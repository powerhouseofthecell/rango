## stage_07
-----
Maybe we should also include the ability to like a post, display its number of likes, and reorder posts by the number of likes they've received?That's what this stage does!

-----
#### Steps Taken
1. Add a like button, and the corresponding AJAX in a Javascript file. But only add the like button on the favorites page.
2. Modify the ```web/urls.py``` to accept a new url with a Favorite object's ID as a parameter
3. Modify ```web/views.py``` to then handle this new url.
4. Modify ```web/models.py``` to add a likes field to our Favorite objects
5. Modify our favorites view in ```web/views.py``` in order to make sure that favorites are actually displayed by number of likes. 
6. Finally, display the number of likes next to the favorite (where should we modify for this?)
