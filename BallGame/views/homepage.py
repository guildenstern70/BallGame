#
#  The Ball Game Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from BallGame.dao import PlayersDAO, UsersDAO
from BallGame.dao.teams_dao import TeamsDAO
from BallGame.settings import BALL_GAME_VERSION
from BallGame.views.ballgame import BallGameView

logger = logging.getLogger(__name__)


class HomePageView(BallGameView):

    template_name = "homepage.html"
    players_db_count = -1
    has_team = False

    def welcome_message(self):
        """
        Get welcome message to display in console
        """
        user_dao = UsersDAO()
        players_dao = PlayersDAO()
        teams_dao = TeamsDAO()
        self.players_db_count = players_dao.count()
        username = self.request.user.username
        welcome = "Welcome to BallGame v." + BALL_GAME_VERSION + ".\n\n"
        if self.players_db_count > 0:
            welcome += "Players DB with " + str(self.players_db_count) + " players.\n"
        else:
            welcome += "Players DB is empty. \nPlease select 'Create Players DB'\n\n"
        user = user_dao.find_user(username)
        if user is not None:
            self.has_team = teams_dao.user_has_team(user)
            if self.has_team:
                welcome += "User " + username + " has a team.\n"
            else:
                welcome += "User " + username + " has not yet a team. \nCreate one with 'Create new team'"
        return welcome

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        welcome = self.welcome_message()
        context['playerscount'] = self.players_db_count
        context['console'] = welcome
        context['has_team'] = self.has_team
        return context
