#
#  The Ball Game Project
#
#  Copyright (c) 2021-24 Alessio Saltarin
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

    def __init__(self):
        super().__init__()
        self.team_players = None
        self.team = None
        self.team_name = None
        self.players_dao = PlayersDAO()
        self.teams_dao = TeamsDAO()
        self.user_dao = UsersDAO()

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.team_name = 'My Team'
        self.team = self.get_team()
        self.team_players = self.players_dao.get_players_in_team(self.team)
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

    def get_filter_kind(self):
        try:
            filter_kind = self.kwargs['kind']
        except KeyError:
            filter_kind = None
        return filter_kind

    def get_queryset(self):
        filter_position = self.get_filter_position()
        filter_kind = self.get_filter_kind()
        if filter_position is not None:
            return self.players_dao.get_available_players_by_position(filter_position)
        if filter_kind is not None:
            if filter_kind.lower() == 'pitchers':
                return self.get_pitchers()
            else:
                return self.get_batters()
        return self.players_dao.get_all_available_players()

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
        context['title'] = 'Team Manager'
        context['team'] = self.team
        context['positions'] = get_positions()
        context['team_players'] = self.team_players
        context['pitchers'] = self.get_pitchers()
        context['batters'] = self.get_batters()
        context['how_many_pitchers'] = len(self.get_pitchers())
        context['how_many_batters'] = len(self.get_batters())
        return context

    def get_pitchers(self):
        if self.team_players is None:
            return []
        unordered_pitchers = [player for player in self.team_players if player.is_pitcher()]
        return self.order_players_by_position(unordered_pitchers, ['SP', 'RP', 'CL', 'SU'])

    def get_batters(self):
        if self.team_players is None:
            return []
        unordered_batters = [player for player in self.team_players if not player.is_pitcher()]
        return self.order_players_by_position(unordered_batters, ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF'])

    @staticmethod
    def order_players_by_position(players, position_order):
        """
        Order players based on the given position order.

        :param players: List of Player objects
        :param position_order: List of positions in the desired order
        :return: Ordered list of Player objects
        """
        position_index = {position: index for index, position in enumerate(position_order)}
        return sorted(players, key=lambda player: position_index.get(player.position, len(position_order)))
