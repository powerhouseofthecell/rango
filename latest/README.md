## stage_03
-----
We've cleaned up and modularized our code a bit more in this stage. We've started including our own custom css files, and we're using more of Django's builtin templating engine's features, such as template extension, to make our code cleaner. We're also using a few more bootstrap features to make everything pretty. 

-----
#### Steps Taken
1. Added a templates directory to the rango directory --> ```rango/templates/```
2. Added ```base.html``` to this new directory --> ```rango/templates/base.html```
3. Extracted common features from ```index.html``` and ```posts.html``` and put these into the new ```base.html``` and then extended this base template to make our new templates much cleaner.
4. Added the use of custom static files to help us customize things a bit more (i.e. writing our own css files)
5. Added a navbar for ease of use.
6. Used the same steps as before in order to run the server and look at our glory.
