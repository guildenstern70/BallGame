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
echo "make migrations..."
python manage.py makemigrations BallGame
echo "migrate..."
python manage.py migrate BallGame
