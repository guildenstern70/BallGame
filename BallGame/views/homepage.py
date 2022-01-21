#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from BallGame.dao import PlayersDAO, UserAttributesDAO, UsersDAO
from BallGame.settings import BALL_GAME_VERSION
from BallGame.views.ballgame import BallGameView

logger = logging.getLogger(__name__)


class HomePageView(BallGameView):
    template_name = "homepage.html"
    userattributes_dao = UserAttributesDAO()
    user_dao = UsersDAO()

    def get_user_data_message(self, userdata):
        """
            Get user data message
        """
        if userdata:
            message = 'Found user data for user = ' + self.request.user.username
        else:
            message = 'No user data found for user = ' + self.request.user.username
        return message

    def get_user_data(self):
        """
        Get user data. Creates one if no user data is found.
        """
        username = self.request.user.username
        logger.info('Getting user data for user = ' + username)
        if not self.userattributes_dao.user_attributes_exists_for(username):
            self.user_dao.create_user_attributes(username)
        user_attributes = self.userattributes_dao.get_user_attributes(username)
        if user_attributes:
            logger.info('Found user data for user = ' + username)
        else:
            logger.info('No user data found for user = ' + username)
        return user_attributes

    def get_context_data(self, **kwargs):
        players_dao = PlayersDAO()
        context = super().get_context_data(**kwargs)
        welcome = "Welcome to BallGame v." + BALL_GAME_VERSION + ".\n\n"
        welcome += "Players DB with " + str(players_dao.count()) + " players.\n"
        user_attributes = self.get_user_data()
        welcome += self.get_user_data_message(user_attributes) + "\n"
        context['console'] = welcome
        context['has_team'] = user_attributes.has_team
        return context
