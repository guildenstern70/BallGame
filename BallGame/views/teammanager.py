#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
from django.views.generic import TemplateView

from BallGame.dao import PlayersDAO
from BallGame.views.ballgame import BallGameView


class NewTeamView(BallGameView):
    template_name = "newteam.html"
    players_dao = PlayersDAO()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Team'
        context['available_players'] = self.players_dao.get_all_players()
        return context
