#
#  The Ball Game Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.contrib.auth import authenticate, login
from django.views.generic import FormView

from BallGame.forms.login_form import LoginForm

logger = logging.getLogger(__name__)


class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = '/home'
    errors = False

    def form_valid(self, form):
        logger.info('Received login form Login Form')
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        logger.info('Username = ' + username)
        user = authenticate(username=username, password=password)
        if user is not None:
            logger.info('User ' + username + ' has been authenticated.')
            login(self.request, user)
            return super().form_valid(form)
        else:
            logger.info('User ' + username + ' is unknown or input wrong password.')
            self.errors = True
            return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        logger.info('Getting context data (errors=' + str(self.errors) + ')')
        context = super(LoginView, self).get_context_data(**kwargs)
        context['errors'] = self.errors
        return context
