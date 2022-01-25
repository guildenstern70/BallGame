#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

from BallGame.models.team import Team


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
        player.team = team
        player.save()

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