#
#  The Ball Game Project
#
#  Copyright (c) 2021 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#


from django.contrib import admin
from django.urls import path

from BallGame import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('another/', views.another, name='another'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
