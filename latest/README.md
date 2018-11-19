## stage_05
-----
Hmm, so we wanted to add more features, like saving our favorite quotes, as well as a few more types of quotes to deal with. In this stage, we've added a model, and we're allowing for some user interaction in order to save our users' favorite posts. We're also letting users pick between lorem ipsum and funny quotes by using the power of urls!

-----
#### Steps Taken
1. We modified the URLs in ```web/urls.py``` in order to allow the URL itself to take some parameters.
2. Then we modified the corresponding view in ```web/views.py```
3. We modified ```rango/templates/base.html``` so that it now lets us use our upgraded URL
4. In ```web/models.py``` we added a Favorite model, with the body of the quote as its only field. 
5. Then we add a view in ```web/views.py``` in order to modify this model when the view is reached
6. We add a URL that will trigger this view.
7. Finally, we add a button to each post and some corresponding AJAX in order to have these buttons submit a GET request to the right url.
