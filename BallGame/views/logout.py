#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.contrib.auth import logout
from django.views.generic import RedirectView

logger = logging.getLogger(__name__)


class LogoutView(RedirectView):

    url = '/'

    def logout(self):
        logger.info('Logging out user ' + str(self.request.user))
        logout(self.request)

    def get_redirect_url(self, *args, **kwargs):
        self.logout()
        return super().get_redirect_url(*args, **kwargs)
