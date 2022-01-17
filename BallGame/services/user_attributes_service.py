#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from BallGame.dao import UsersDAO
from BallGame.dao.userattributes_dao import UserAttributesDAO
from BallGame.models import UserAttributes

logger = logging.getLogger(__name__)


def create_user_attributes(request_user):
    logging.info('Creating User Attributes for User = ' + request_user)
    userdao = UsersDAO()
    user = userdao.get_user(request_user)
    user_attr = UserAttributes.create(False, user)
    user_attr.save()


def get_user_data(request):
    """
    Get user data. May return None if no user data is found.
    """
    username = request.user.username
    logger.info('Getting user data for user = ' + username)
    user_attributes = UserAttributesDAO()
    if user_attributes.userdata_exists_for(username):
        user_data = user_attributes.get_user_data(username)
    else:
        create_user_attributes(username)
        user_data = user_attributes.get_user_data(username)
    if user_data:
        logger.info('Found user data for user = ' + username)
    else:
        logger.info('No user data found for user = ' + username)
    return user_data


def get_user_data_message(request):
    """
        Get user data message
    """
    message = 'No user data found for user = ' + request.user.username
    if get_user_data(request):
        message = 'Found user data for user = ' + request.user.username
    return message
