#
#  The Ball Game Project
#
#  Copyright (c) 2021-24 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging
from django.views.generic import RedirectView

from BallGame.utils import create_players_db

logger = logging.getLogger(__name__)


class CreatePlayersView(RedirectView):

    url = '/home'

    def get_redirect_url(self, *args, **kwargs):
        logger.info('Creating players DB... ')
        create_players_db()
        logger.info('Done.')
        return super().get_redirect_url(*args, **kwargs)
