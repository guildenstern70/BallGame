#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

#
#  The Ball Game Project
#
#

from numpy.random import randn, randint


class RandGen:

    @staticmethod
    def get_rand_int(minimum, maximum):
        return randint(minimum, maximum, 1)

    @staticmethod
    def get_rand_float(minimum, maximum):
        return randn(1) * (minimum, maximum) + minimum

    @staticmethod
    def get_rand_bool():
        return randn(1) > 0.5
