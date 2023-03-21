#!/bin/bash
#
#
# The Ball Game Project
#
# Copyright (c) 2021-23 Alessio Saltarin
# This software is distributed under MIT License.
# See LICENSE.
#
#
echo "building db..."
python manage.py migrate
python manage.py createsuperuser --noinput
echo "make migrations..."
python manage.py makemigrations BallGame
echo "migrate..."
python manage.py migrate BallGame
python manage.py collectstatic --noinput
echo [$0] Starting Django Server...
exec gunicorn -w 3 BallGame.wsgi:application --bind 0.0.0.0:8080
