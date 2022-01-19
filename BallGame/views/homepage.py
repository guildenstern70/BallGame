#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

from BallGame.services import get_user_data_message
from BallGame.settings import BALL_GAME_VERSION
from BallGame.utils import db_players_count
from BallGame.views.ballgame import BallGameView


class HomePageView(BallGameView):

    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        welcome = "Welcome to BallGame v." + BALL_GAME_VERSION + ".\n\n"
        welcome += "Players DB with " + db_players_count() + " players.\n"
        welcome += get_user_data_message(request) + "\n"
        context['console'] = welcome

        return context
