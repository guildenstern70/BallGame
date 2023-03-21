#
#  The Ball Game Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

from BallGame.dao import PlayersDAO
from BallGame.models.team import Team

import logging

logger = logging.getLogger(__name__)


class TeamsDAO:

    def count(self):
        return self._model.objects.count()

    @staticmethod
    def create_new_team(name, user):
        newteam = Team.create(name=name, user=user)
        newteam.save()
        return newteam

    @staticmethod
    def add_player_to_team(team, player):
        if player.team != team:
            player.team = team
            player.save()
            logger.info("Player %s added to team %s", player.last_name, team.name)
        else:
            logger.info("Player %s is already in team %s", player.last_name, team.name)

    def add_player_to_team_ids(self, team_id, player_id):
        """ Add player id to team id. Return True if operation succeeded """
        try:
            team = self._model.objects.get(id=team_id)
            playersdao = PlayersDAO()
            player = playersdao.find_by_id(player_id)
            self.add_player_to_team(team, player)
            return True
        except ObjectDoesNotExist:
            return False

    def delete(self, team):
        dbteam = self._model.objects.get(id=team.id)
        dbteam.delete()

    @staticmethod
    def remove_player_from_team(player):
        player.team = None
        player.save()

    def find_by_name(self, name):
        try:
            return self._model.objects.get(name=name)
        except ObjectDoesNotExist:
            return None

    def get_user_team(self, user):
        try:
            team = self._model.objects.get(user=user)
        except ObjectDoesNotExist:
            return None
        return team

    def user_has_team(self, user):
        try:
            team = self._model.objects.get(user=user)
            if team is None:
                return False
        except ObjectDoesNotExist:
            return False
        return True

    def __init__(self):
        """ Constructor """
        self._model = apps.get_model('BallGame', 'Team')
