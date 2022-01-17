#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
#

from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist


class UserAttributesDAO:
    """
    UserAttributes DAO
    """

    def get_user_data(self, request_user):
        return self._model.objects.get(user__username=request_user)

    def userdata_exists_for(self, request_user):
        try:
            if self._model.objects.get(user__username=request_user):
                return True
        except ObjectDoesNotExist:
            return False
        return False

    def __repr__(self):
        return "Object of UserAttributesDAO"

    def __init__(self):
        """ Constructor """
        self._model = apps.get_model('BallGame', 'UserAttributes')
