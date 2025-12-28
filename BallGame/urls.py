"""
URL configuration for BallGame project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from BallGame.views.redirects.addplayer import AddPlayerView
from BallGame.views.redirects.createplayers import CreatePlayersView
from BallGame.views.homepage import HomePageView
from BallGame.views.index import IndexView
from BallGame.views.login import LoginView
from BallGame.views.redirects.logout import LogoutView
from BallGame.views.registration import RegistrationView, RegistrationOkView
from BallGame.views.teamlist import TeamListView

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
    path('teamlist/', login_required(TeamListView.as_view()), name='team-list'),
    path('teamlist/bypos/<str:position>', login_required(TeamListView.as_view()), name='team-list'),
    path('teamlist/bykind/<str:kind>', login_required(TeamListView.as_view()), name='team-list'),
]

