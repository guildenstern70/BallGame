#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.apps import apps

logger = logging.getLogger(__name__)


def get_positions():
    """
    Get baseball positions
    """
    return ['P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF']


class PlayersDAO:

    def count(self):
        return self._model.objects.count()

    def get_all_players(self):
        return self._model.objects.all()

    def get_players_by_position(self, position):
        return self._model.objects.filter(position=position)

    def __init__(self):
        """ Constructor """
        self._model = apps.get_model('BallGame', 'Player')



