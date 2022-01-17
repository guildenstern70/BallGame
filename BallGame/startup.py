#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging
from django.apps import AppConfig, apps

logger = logging.getLogger(__name__)


class Startup(AppConfig):
    """
    Code to run on application startup.
    """
    logger.info("Welcome to BallGame")
    name = 'BallGame'
    verbose_name = "Baseball Sim"


