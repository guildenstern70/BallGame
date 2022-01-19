#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
from django.views.generic import TemplateView

from BallGame.settings import BALL_GAME_VERSION


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BallGame'
        context['version'] = BALL_GAME_VERSION
        return context
