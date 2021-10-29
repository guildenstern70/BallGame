#
#  The Ball Game Project
#
#  Copyright (c) 2021 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from BallGame.services import get_user_data

logger = logging.getLogger(__name__)


def index(request):
    template = loader.get_template('index.html')
    context = {
        'title': 'BallGame',
        'version': '0.1'
    }
    return HttpResponse(template.render(context, request))


def login_view(request):
    logger.info('Login form.')
    errors = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        logger.info('Received login form POST')
        logger.info('Username = ' + username)
        user = authenticate(username=username, password=password)
        if user is not None:
            logger.info('User ' + username + ' was authenticated.')
            login(request, user)
            return HttpResponseRedirect('/home/')
        else:
            logger.info('User ' + username + ' is unknown or input wrong password.')
            errors = True
    template = loader.get_template('account/login.html')
    context = {
        'title': 'Login',
        'header': 'Login',
        'errors': errors
    }
    return HttpResponse(template.render(context, request))


@login_required
def logout_view(request):
    logger.info('Logging out user ' + str(request.user))
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    template = loader.get_template('homepage.html')
    # Initialize user if not done yet
    context = {
        'title': 'Homepage',
        'username': request.user.username,
        'userdata': get_user_data(request)
    }
    return HttpResponse(template.render(context, request))



