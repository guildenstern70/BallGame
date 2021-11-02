#
#  The Ball Game Project
#
#  Copyright (c) 2021 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging
from os.path import exists
from django.apps import AppConfig, apps
from BallGame.services import create_player, get_positions, load_data_from_file

logger = logging.getLogger(__name__)


class Startup(AppConfig):
    """
    Code to run on application startup.
    """
    name = 'BallGame'
    verbose_name = "Baseball Sim"


