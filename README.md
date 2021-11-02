# BallGame

A statistical baseball simulation.

#### Admin App

If not already done, create super-user with

    python manage.py createsuperuser
    
If unsure, try with "admin/admin"

### Setup

To create and populate the database run:

    python manage.py migrate
    python manage.py makemigrations BallGame
    python manage.py migrate BallGame


