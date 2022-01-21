#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
#
import logging

from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)


class UserAttributesDAO:
    """
    UserAttributes DAO
    """

    def get_user_attributes(self, request_user):
        return self._model.objects.get(user__username=request_user)

    def user_attributes_exists_for(self, request_user):
        try:
            if self._model.objects.get(user__username=request_user):
                return True
        except ObjectDoesNotExist:
            return False
        return False

    def __init__(self):
        """ Constructor """
        self._model = apps.get_model('BallGame', 'UserAttributes')
