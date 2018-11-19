#!/bin/bash

# this file tells the server how to run Django, and we use waitress for this example, at least to deploy to Heroku
waitress-serve --port=$PORT latest/rango.wsgi:application
