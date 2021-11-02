#
#  The Ball Game Project
#
#  Copyright (c) 2021 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import random

from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    position = models.CharField(max_length=3)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()

    @classmethod
    def create(cls, position, first_names, last_names):
        """
        Create a new player
        """
        player = cls(position=position)
        player.age = random.randint(17, 35)
        player.first_name = random.choice(first_names)
        player.last_name = random.choice(last_names)
        player.height = random.randint(160, 210)
        player.weight = random.randint(58, 120)
        return player

    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + self.position + ")"


