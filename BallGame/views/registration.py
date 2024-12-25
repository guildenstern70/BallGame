#
#  The Ball Game Project
#
#  Copyright (c) 2021-24 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView

from BallGame.forms.registration_form import RegistrationForm
from BallGame.views.ballgame import BallGameMixin

logger = logging.getLogger(__name__)


class RegistrationOkView(BallGameMixin, TemplateView):
    template_name = "account/registration_ok.html"

    def get_context_data(self, **kwargs):
        username = self.kwargs['username']
        if username is None:
            username = '?'
        context = super().get_context_data(**kwargs)
        context['username'] = username
        return context


class RegistrationView(FormView):
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = '/registration_ok'
    errors = False

    def form_valid(self, form):
        registration_data = form.cleaned_data
        logger.info('Received registration data...')
        registered_user = registration_data['username']
        logger.info('Registering user ' + registered_user + '...')
        form.save()
        return HttpResponseRedirect('/registered/' + registered_user)

