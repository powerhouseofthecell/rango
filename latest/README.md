## stage_06
-----
Oops! We've been favoriting all these quotes, but we still haven't actually displayed them to the user. Let's add a new favorites page using all that we know about templates and URLs in Django, and then we're going to access the models we have and display these favorites to the user! (Some cute Javascript included for free!)

-----
#### Steps Taken
1. Add a new template to our ```web/templates/``` called ```favorites.html``` --> ```web/templates/favorites.html```
2. Modify this template to allow us to print out all the favorited posts (very similar to the posts template)
3. Add a favorites view to ```web/views.py```
4. Add a corresponding URL to ```web/urls.py``` so that we can get to that view. 
5. Update ```rango/templates/base.html``` to reflect the addition of this new url (a la navbar)
