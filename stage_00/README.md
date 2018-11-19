## stage_00
-----
This is the very first stage. It represents an initial install and project with Django, with no configuration complete. If you run ```waitress-serve rango.wsgi:application``` or set the environment variable ```PORT``` to your favorite port number and then run ```sh run.sh``` you will be able to run this first stage locally on your computer. However, this assumes that you have installed the requirements with ```pip install -r requirements.txt```. Once those are installed, the above two versions of the same command should work just fine, and you should see some form of "Congratulations" when you go to ```127.0.0.1:YOURPORT``` in your web browser of choice. 

-----
#### Steps Taken
1. Installed dependencies with ```pip install -r requirements.txt```
2. Ran ```django-admin startproject rango``` to create the initial project directories. 
3. Ran the actual webserver via waitress by navigating into the new project and running ```waitress-serve --port=8888 rango.wsgi:application```
4. Marvelled at the beauty that is Django's initial page by going and visiting ```127.0.0.1:8888```