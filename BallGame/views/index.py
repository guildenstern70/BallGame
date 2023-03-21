#
#  The Ball Game Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

from BallGame.settings import BALL_GAME_VERSION
from BallGame.views.ballgame import BallGameView


class IndexView(BallGameView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BallGame'
        context['version'] = BALL_GAME_VERSION
        return context
