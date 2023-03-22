#
#  The Ball Game Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.shortcuts import redirect
from django.views.generic import ListView

from BallGame.dao import PlayersDAO, UsersDAO
from BallGame.dao.teams_dao import TeamsDAO
from BallGame.models import Player
from BallGame.utils import get_positions
from BallGame.views.ballgame import BallGameMixin

logger = logging.getLogger(__name__)


class TeamListView(BallGameMixin, ListView):
    model = Player
    template_name = "teamlist.html"
    players_dao = PlayersDAO()
    teams_dao = TeamsDAO()
    user_dao = UsersDAO()
    team_name = "My team"
    team_players = None

    def dispatch(self, request, *args, **kwargs):
        players_db_count = self.players_dao.count()
        if players_db_count <= 0:
            logger.info('Players DB is empty. Redirecting to home.')
            return redirect('home')
        return super(TeamListView, self).dispatch(request, *args, **kwargs)

    def get_filter_position(self):
        try:
            filter_position = self.kwargs['position']
        except KeyError:
            filter_position = None
        return filter_position

    def get_queryset(self):
        filter_position = self.get_filter_position()
        if filter_position is None:
            return self.players_dao.get_all_available_players()
        return self.players_dao.get_available_players_by_position(filter_position)

    def get_team(self):
        user = self.request.user
        team = None
        if user is not None:
            has_team = self.teams_dao.user_has_team(user)
            if not has_team:
                logger.info('User ' + user.username + ' does not own a team')
                logger.info('Creating new one...')
                team = self.teams_dao.create_new_team(self.team_name, user)
                logger.info('Done.')
            else:
                team = self.teams_dao.get_user_team(user)
        return team

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_ballgame_context(context)
        team = self.get_team()
        context['title'] = 'Team Manager'
        context['team'] = team
        context['positions'] = get_positions()
        context['team_players'] = self.players_dao.get_players_in_team(team)
        return context
