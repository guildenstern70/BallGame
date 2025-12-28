#
#  The Ball Game Project
#
#  Copyright (c) 2021-24 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
from random import randrange, random


class RandGen:

    @staticmethod
    def get_rand_int(minimum, maximum):
        return randrange(minimum, maximum, 1)

    @staticmethod
    def get_rand_float(minimum, maximum):
        return random() * (minimum, maximum) + minimum

    @staticmethod
    def get_rand_bool():
        return random() > 0.5
