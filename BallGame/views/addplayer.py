#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.views.generic import RedirectView

from BallGame.dao.teams_dao import TeamsDAO

logger = logging.getLogger(__name__)


class AddPlayerView(RedirectView):

    url = '/team'

    def get_redirect_url(self, *args, **kwargs):
        logger.info('Adding player to team... ')
        teamid = kwargs['team_id']
        playerid = kwargs['player_id']
        if playerid is not None and teamid is not None:
            teamsdao = TeamsDAO()
            if not teamsdao.add_player_to_team_ids(teamid, playerid):
                logger.error('Cannot add player ' + str(playerid) + ' to team ' + str(teamid))
        return super().get_redirect_url(*args, **kwargs)
