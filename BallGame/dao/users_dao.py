#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
#
import logging

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from BallGame.models import UserAttributes

logger = logging.getLogger(__name__)


class UsersDAO:
    """
    Users DAO
    """

    def find_user(self, user_name):
        try:
            return self._model.objects.get(username=user_name)
        except ObjectDoesNotExist:
            return None

    def create_user_attributes(self, request_user):
        logging.info('Creating User Attributes for User = ' + request_user)
        user = self.find_user(request_user)
        user_attr = UserAttributes.create(False, user)
        user_attr.save()

    def __init__(self):
        """ Constructor """
        self._model = get_user_model()
