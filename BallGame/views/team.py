#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.shortcuts import redirect

from BallGame.dao import PlayersDAO, UsersDAO
from BallGame.dao.teams_dao import TeamsDAO
from BallGame.views.ballgame import BallGameView

logger = logging.getLogger(__name__)


class TeamView(BallGameView):
    template_name = "team.html"
    players_dao = PlayersDAO()
    teams_dao = TeamsDAO()
    team_name = "My team"
    team_players = None

    def create_new_team(self, user):
        return self.teams_dao.create_new_team(self.team_name, user)

    def dispatch(self, request, *args, **kwargs):
        players_db_count = self.players_dao.count()
        if players_db_count <= 0:
            logger.info('Players DB is empty. Redirecting to home.')
            return redirect('home')
        return super(TeamView, self).dispatch(request, *args, **kwargs)

    def get_team(self):
        user_dao = UsersDAO()
        username = self.request.user.username
        user = user_dao.find_user(username)
        team = None
        if user is not None:
            has_team = self.teams_dao.user_has_team(user)
            if not has_team:
                logger.info('User ' + username + ' does not own a team')
                logger.info('Creating new one...')
                team = self.create_new_team(user)
                logger.info('Done.')
            else:
                team = self.teams_dao.get_user_team(user)
        return team

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = self.get_team()
        context['title'] = 'Team Manager'
        context['team_name'] = team.name
        context['team_players'] = self.players_dao.get_players_in_team(team)
        context['available_players'] = self.players_dao.get_all_players()
        return context
