#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#


from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from BallGame.views.homepage import HomePageView
from BallGame.views.index import IndexView
from BallGame.views.login import LoginView
from BallGame.views.logout import LogoutView
from BallGame.views.registration import RegistrationView, RegistrationOkView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('registered/<str:username>', RegistrationOkView.as_view(), name='registration_ok'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', login_required(HomePageView.as_view()), name='home'),
]

