#
#  The Ball Game Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
from django.views.generic import TemplateView

from BallGame.settings import BALL_GAME_VERSION


class BallGameView(TemplateView):

    def get_context_data(self, **kwargs):
        username = self.request.user.username
        if username is None:
            username = '?'
        context = super().get_context_data(**kwargs)
        context['title'] = 'BallGame'
        context['username'] = username
        context['version'] = BALL_GAME_VERSION
        return context
