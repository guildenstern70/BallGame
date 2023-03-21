# BallGame

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![BallGame CI](https://github.com/guildenstern70/BallGame/actions/workflows/ballgame.yml/badge.svg)](https://github.com/guildenstern70/BallGame/actions/workflows/ballgame.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2f8278ac384f478598006b058249b4e9)](https://www.codacy.com/gh/guildenstern70/BallGame/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=guildenstern70/BallGame&amp;utm_campaign=Badge_Grade)


A statistical baseball simulation.

### Admin App

If not already done, create super-user with

    python manage.py createsuperuser
    
If unsure, try with "admin/admin"

### Setup

Install Python libraries:

    pip install -r requirements.txt

To create and populate the database run: (delete the database file if it already exists)

    ./setup.sh

### How the players database is created

The database player is created when running the second migration, 'player_userattributes'.

### Virtual Environment

Activate with

    source ./venv/bin/activate

Deactivate with

    deactivate

### Crispy Forms

This project uses Crispy Forms for Bootstrap:

    https://django-crispy-forms.readthedocs.io/en/latest/

