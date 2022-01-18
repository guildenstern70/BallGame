#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
#

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


class UsersDAO:
    """
    Users DAO
    """

    def find_user(self, user_name):
        try:
            return self._model.objects.get(username=user_name)
        except ObjectDoesNotExist:
            return None

    def __init__(self):
        """ Constructor """
        self._model = get_user_model()
