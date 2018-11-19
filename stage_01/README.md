## stage_01
-----
This stage sets up our initial flow from user visiting to a view response. It also gets our development static deployable to Heroku. However, this way of serving static files is extremely not recommended (as noted in the ```settings.py``` comments), since usage of a content delivery network or CDN is preferred. For simplicity sake, we will be using the development version here (the secret key is even included in version control, or Git, which also shouldn't happen in production). This stage is intended to familiarize you with how Django's basic flow works. 

-----
#### Steps Taken
1. Installed a new app with ```django-admin startapp web``` # this will be our web application
2. Added the correct settings to our ```rango/settings.py``` file for staticfiles, at least for development purposes (examine the bottom of ```rango/settings.py``` to see)
3. Copied ```rango/urls.py``` to ```web/urls.py``` and then imported the views in ```web/views.py``` so that we can send requests to the appropriate views. 
4. Modified ```rango/urls.py``` to match the appropriate URL requests to either admin, our web app, or the static files directories. 
5. Set up a simplified view in ```web/views.py``` that simply returns a "Hello, world!" response upon going to any webpage.
6. Took a gander and were greeted by "Hello, world!" in beautiful bold by running the server (```python3 manage.py serve 0.0.0.0 8888```) and then visiting ```127.0.0.1:8888```. 
