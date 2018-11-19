## stage_02
-----
Finally, we get to write a little bit of HTML! We've introduced some templating syntax, and we've made our URLs a bit more interesting. We have also started the process of creating some interesting posts in our rango blog. We introduce some basic Bootstrap, but since that's not the main point of the tutorial, we won't talk about it very much (they have fantastic documentation online).

-----
#### Steps Taken
1. Added the web app to our INSTALLED_APPS in ```rango/settings.py```
2. Created a templates directory in ```web``` --> ```web/templates/``` and then added ```index.html``` to it (stylized with Bootstrap)
3. Added another template called ```posts.html``` to our templates directory, and stylized it with Bootstrap. We also introduced the use of the templating engine language in order to render some content brought in from the view (the double "{{" syntax). 
4. Added a view in ```web/views.py``` that allowed us to render this new template, with some hardcoded Lorem Ipsum content.
5. Added the corresponding URL path to allow us as the user to actually access this new template in ```web/urls.py```
6. Followed similar steps to those in previous stages in order to run the actual app and view our work. 
