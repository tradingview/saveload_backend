Charting Library Save/Load Backend
================

This is the tiny backend implementing Charting Library charts storage.

## Requirements
Python 3x, pip, Django, Postgresql

## How to start

1. Install Python 3.x and Pip. Use virtual environment if your host has older python version and it cant be upgraded.
2. Install PostgreSQL or some other Django-friendly database engine. Also you might want to install PgAdmin or any other administrative tool for your database.
3. Go to your charts storage folder and run `pip install -r requirements.txt`. Unix users : you have to have python-dev package to install `psycopg2`.
4. Create an empty database in Postgres (using either command line or `pgadmin`). Go to `charting_library_charts` folder and set up your database connection in `settings.py` (see `DATABASES` @ line #12).
5. Run `python manage.py migrate`. This will create database schema without any data.
6. Run `python manage.py runserver` to run *TEST* instance of your database. Use some other stuff (i.e., Gunicorn) for your production environment.

