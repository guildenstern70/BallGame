#
#  The Ball Game Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#


from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from BallGame.views.addplayer import AddPlayerView
from BallGame.views.createplayers import CreatePlayersView
from BallGame.views.homepage import HomePageView
from BallGame.views.index import IndexView
from BallGame.views.login import LoginView
from BallGame.views.logout import LogoutView
from BallGame.views.registration import RegistrationView, RegistrationOkView
from BallGame.views.team import TeamView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('player/<str:action>/<int:team_id>/<int:player_id>', AddPlayerView.as_view(), name='player'),
    path('createdb/', CreatePlayersView.as_view(), name='createdb'),
    path('home/', login_required(HomePageView.as_view()), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('registered/<str:username>', RegistrationOkView.as_view(), name='registration_ok'),
    path('team/', login_required(TeamView.as_view()), name='team'),
    path('team/<str:position>', login_required(TeamView.as_view()), name='team'),
]

