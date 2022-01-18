# BallGame

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


A statistical baseball simulation.

### Admin App

If not already done, create super-user with

    python manage.py createsuperuser
    
If unsure, try with "admin/admin"

### Setup

To create and populate the database run:

    python manage.py migrate
    python manage.py makemigrations BallGame
    python manage.py migrate BallGame

### How the players database is created

The database player is created when running the second migration, 'player_userattributes'.

### Virtual Environment

Activate with

    source ./venv/bin/activate

Deactivate with

    deactivate

