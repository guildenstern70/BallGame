#
#  The Ball Game Project
#
#  Copyright (c) 2021 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.apps import apps

logger = logging.getLogger(__name__)


def get_user_data(request):
    """
    Get user data
    """
    logger.info('Getting user data for user = ' + request.user.username)
    user_attributes = apps.get_model('BallGame', 'UserAttributes')
    user_data = user_attributes.objects.get_or_create(user=request.user)[0]
    if user_data:
        logger.info('Found user data for user = ' + user_data.user.username)
    else:
        logger.info('No user data found for user = ' + request.user.username)
    return user_data

