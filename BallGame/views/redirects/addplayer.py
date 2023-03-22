#
#  The Ball Game Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.views.generic import RedirectView

from BallGame.dao.teams_dao import TeamsDAO

logger = logging.getLogger(__name__)


def add_player(teamid, playerid):
    if playerid is not None and teamid is not None:
        teamsdao = TeamsDAO()
        if not teamsdao.add_player_to_team_ids(teamid, playerid):
            logger.error('Cannot add player ' + str(playerid) + ' to team ' + str(teamid))


def remove_player(playerid):
    if playerid is not None:
        TeamsDAO.remove_player_from_team(playerid)


class AddPlayerView(RedirectView):
    url = '/teamlist'

    def get_redirect_url(self, *args, **kwargs):
        logger.info('Adding/Removing player to team... ')
        action = kwargs['action']  # Add or Remove
        teamid = kwargs['team_id']
        playerid = kwargs['player_id']
        if action == 'add':
            add_player(teamid, playerid)
        else:
            remove_player(playerid)
        return super().get_redirect_url(*args, **kwargs)
