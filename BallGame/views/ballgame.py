#
#  The Ball Game Project
#
#  Copyright (c) 2021-24 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

from BallGame.settings import BALL_GAME_VERSION


class BallGameMixin:
    """
    This mixin allows Django views to get a context
    already populated with BallGame template items, such as
        - Logged User
        - App Title
        - App Version
    This mixin has to be used *only* with Django views with self.request
    populated.
    """

    def get_ballgame_context(self, context):
        username = self.request.user.username
        if username is None:
            username = '?'
        context['title'] = 'BallGame'
        context['username'] = username
        context['version'] = BALL_GAME_VERSION
        return context
