# BallGame

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![BallGame CI](https://github.com/guildenstern70/BallGame/actions/workflows/ballgame.yml/badge.svg)](https://github.com/guildenstern70/BallGame/actions/workflows/ballgame.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2f8278ac384f478598006b058249b4e9)](https://www.codacy.com/gh/guildenstern70/BallGame/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=guildenstern70/BallGame&amp;utm_campaign=Badge_Grade)


A statistical baseball simulation.

### Setup

Install Python libraries:

    uv sync

To create and populate the database run: (delete the database file if it already exists)

1. Migrate to saved state

```bash
echo "migrate..."
python manage.py migrate
```

2. Publish migrations and migrate BallGame app

```bash
echo "make migrations..."
python manage.py makemigrations BallGame
python manage.py migrate BallGame
```

### Admin App

If not already done, create super-user with

    python manage.py createsuperuser
    
If unsure, try with "admin/admin"

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
