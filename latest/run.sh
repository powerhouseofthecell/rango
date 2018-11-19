#!/bin/bash

# this file tells the server how to run Django, and we use waitress for this example, at least to deploy to Heroku
python3 latest/manage.py makemigrations
python3 latest/manage.py migrate
python3 latest/manage.py serve 0.0.0.0 $PORT
