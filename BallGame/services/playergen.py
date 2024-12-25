# 
#  The Ball Game Project
# 
#  Copyright (c) 2021-24 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
from BallGame.services.randgen import RandGen


class PlayerGenerator:

    def __init__(self, player):
        self.randgen = RandGen()
        self.player = player

    def shape(self):
        self.player.age = self.randgen.get_rand_int(17, 42)
        self.player.height = self.randgen.get_rand_int(160, 210)
        self.player.weight = self.randgen.get_rand_int(58, 120)
        self.player.speed = self.randgen.get_rand_int(0, 100)
        self.player.pitch_quality = self.get_quality(True)
        self.player.pitch_control = self.get_quality(True)
        self.player.pitch_movement = self.get_quality(True)
        self.player.pitch_stamina = self.get_quality(True)
        self.player.bat_contact = self.get_quality(False)
        self.player.bat_power = self.get_quality(False)
        self.player.bat_eye = self.get_quality(False)
        self.player.bat_defense = self.get_quality(False)
        return self.player

    def get_quality(self, is_pitch_attribute):
        """
        Return the player's quality attribute.
        Sets qualities according to position.
        """
        max_attr = 40
        if self.player.is_pitcher():
            if is_pitch_attribute:
                max_attr = 100
        else:
            if not is_pitch_attribute:
                max_attr = 100
        return self.randgen.get_rand_int(0, max_attr)
