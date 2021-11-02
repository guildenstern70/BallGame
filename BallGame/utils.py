#
#  The Ball Game Project
#
#  Copyright (c) 2021 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

#
#  The Ball Game Project
#
#
import logging
import random

from BallGame.models import Player

logger = logging.getLogger(__name__)


def get_positions():
    """
    Get baseball positions
    """
    return ['P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF']


def load_data_from_file(filename):
    """
    Load data from file
    """
    logger.info('Loading data from file = ' + filename)
    line_count = 0
    lines = []
    with open(filename) as file_in:
        for line in file_in:
            line_count += 1
            lines.append(line.lower().strip().capitalize())
    return lines


def create_players_db(apps, schema_editor):
    players = apps.get_model('BallGame', 'Player')
    if players.objects.count() == 0:
        logger.info("Creating players database...")
        logger.info("  Loading resources...")
        first_names = load_data_from_file('resources/male-first-names.txt')
        last_names = load_data_from_file('resources/last-names.txt')
        logger.info("  Done loading resources.")
        for position in get_positions():
            player = Player.create(position, first_names, last_names)
            logger.info("Created player: %s", str(player))
            player.save(player)
        logger.info("Done creating players database.")

