#
#  The Ball Game Project
#
#  Copyright (c) 2021-24 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.apps import apps

logger = logging.getLogger(__name__)


class PlayersDAO:

    def count(self):
        return self._model.objects.count()

    def find_by_id(self, player_id):
        return self._model.objects.get(id=player_id)

    def get_all_players(self):
        return self._model.objects.all()

    def get_all_available_players(self):
        return self._model.objects.filter(team__isnull=True)

    def get_players_in_team(self, team):
        return self._model.objects.filter(team=team)

    def get_players_by_position(self, position):
        return self._model.objects.filter(position=position)

    def get_available_players_by_position(self, position):
        return self._model.objects.filter(team__isnull=True).filter(position=position)

    def __init__(self):
        """ Constructor """
        self._model = apps.get_model('BallGame', 'Player')



