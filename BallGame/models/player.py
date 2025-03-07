#
#  The Ball Game Project
#
#  Copyright (c) 2021-24 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import random

from django.db import models

from BallGame.models.team import Team
from BallGame.services.playergen import PlayerGenerator


class Player(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    position = models.CharField(max_length=3)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    speed = models.IntegerField(default=0)
    bat_contact = models.IntegerField(default=0)
    bat_power = models.IntegerField(default=0)
    bat_eye = models.IntegerField(default=0)
    bat_defense = models.IntegerField(default=0)
    pitch_quality = models.IntegerField(default=0)
    pitch_control = models.IntegerField(default=0)
    pitch_movement = models.IntegerField(default=0)
    pitch_stamina = models.IntegerField(default=0)

    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)

    def is_pitcher(self):
        return self.position == "CL" or self.position == "RP" or self.position == "SP" or self.position == "SU"

    @classmethod
    def create(cls, position, first_names_collection, last_names_collection):
        """
        Create a new player
        """
        player = cls(position=position)
        player.first_name = random.choice(first_names_collection)
        player.last_name = random.choice(last_names_collection)
        player.team = None
        return PlayerGenerator(player).shape()

    def get_pitcher_value(self):
        if self.is_pitcher():
            value = (self.pitch_quality + self.pitch_control + self.pitch_movement + self.pitch_stamina) / 4
            return f"{value:.2f}"
        return 0.0

    def get_batter_value(self):
        if not self.is_pitcher():
            value = (self.bat_contact + self.bat_power + self.bat_eye + self.bat_defense) / 4
            return f"{value:.2f}"
        return 0.0

    def __str__(self):
        is_pitcher = self.is_pitcher()
        if is_pitcher:
            return self.position + " - " + self.first_name + " " + self.last_name + " [" + self.get_pitcher_value() + "Mln $]"
        else:
            return self.position + " - " + self.first_name + " " + self.last_name + " [" + self.get_batter_value() + "Mln $]"


