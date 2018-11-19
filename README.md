# Random. Django. Rango.

-----
### Introduction

This is a basic introduction to building a website with Python and the Django framework. If you've never developed a website before, this is a decent way to get your feet wet with low commitment and relatively simple concepts that go a long way towards understanding what exactly is behind some of the world's websites. 

Enjoy!

-----
### What is Django?

Django is a web development framework written in Python meant for "rapid development and clean, pragmatic design" according to their homepage, which is located [here](https://www.djangoproject.com "Django's Homepage"). Roughly speaking, it's a quick and easy way to build websites for the tech-savvy and time-crunched developer. 

-----
### Why Django?

Well...I think it's cool. Seriously, it's just a very elegantly written framework that gives me easy access to a bunch of very clean and convenient tools, from Cross Site Request Forgery protection, to clean URLs and request management. Overall, I simply enjoy that the framework is designed to be modular - I manage my URLs in one set of files, I give access to certain hosts in another file, and I manage how certain requests and URLs are handled in another file. This separation of responsibilities makes development with a team rather easy, and even for personal projects, Django is quite quick and easy to use. 

-----
### MVT

Models. Views. Templates. Not quite the "beets, bears, battlestar galactica" of The Office's Dwight, but this is one of the fundamental idea trios to the Django framework. In general, MVT is usually called "MVC" for Models, Views, and Controllers; however, Django has the MVT paradigm, and that is what we will explain here.

#### Models
Models are our data, we use them to interact with the database underlying data, and they're set up in the ```models.py``` files of each of our respective apps (we'll talk about the Django structure in a sec). One of my favorite parts about how Django sets up models is that you don't need to write _any_ actual database queries. Everything is Python, and each model in Django is simply a Python class. Already familiar with Python classes? Congrats, you're also now familiar with Django's database structures. 

#### Views
These are how we handle requests. Want to return error on any POST request that comes through your index page? Handle it in a view. GET requests to "https://my_site/quick_ways_to_make_money"? Put those tips in a view. Views are designed and set up in each app's respective ```views.py``` file, and they're not too terrible to understand. They're Python functions that take in a request object (this is the object that holds our input data if we have a form submission for example), and they return some form of HTTP response (maybe a rendered template, for example). That is, this is how they work in their simplest form. We can configure them to be even more powerful if we modify what parameters the URL sends to them (which we will totally do in this demo). But tl;dr, views are Python functions that let you control your website's behavior. Boom. 

#### Templates
Technically, this is the appearance and HTML of the website. But it's really so much more than that. With Django's templating engine, it's almost like you get to write Python code in HTML. However, this templating engine code allows you to generate HTML code with the snap of you fingers. It also lets you reuse base code to keep all of your webpages super consistent and beautiful. I love myself some reusability, and Django has lots of it. I've heard the phrase "never rewrite code" a few too many times in my life (thanks CS51), but it's a great rule of thumb, and Django makes it possible even in HTML. 

-----
### Django's Tango
The way Django likes to do things is pretty convenient for the casual developer/team. The structure is essentially that you create a project root with ```django-admin startproject myprojectlol```, and then you add on specialized apps for that project with ```django-admin startapp web|api|otherstuff|coolstuff|etc```. Then, you configure the settings for these apps and project in ```myprojectlol/settings.py```. Each app has a ```models.py```, a ```views.py```, and I generally add a ```urls.py``` to each app just to make things a little more modular. There's also some other pieces that are convenient for the production team, but we won't be discussing them much here. In fact, there's an entire world to Django from custom tags and filters to testing-integration that we won't cover, but are super awesome features of Django that you should check out as you get more familiar with it. Beyond that, the structure isn't too terrible to understand, and as we build it up, you should start to get an intuition for how it all fits together. 

-----
### Cool, so what're we building?

Ever wanted to build a blog for the sake of teaching a bunch of people how to use Django, but you're too lazy to write content for the blog yourself? Me too. And that's kinda what we'll be doing. We want to build a blog...of sorts. So we're going to leverage all sorts of nifty resources and things here to let us build a sort of "procedural blog." Unfortunately, we can't just copy random blogs from around the Internet and steal their ideas due to something called "plagiarism," so we're going to explore with the help of some API's how Django can be used to make a really really random blog in Django. And I'm calling it "Rango." If you don't like my puns, I'm sorry, but I cannot help it. 

-----
### Weird Flex, but Ok, how do I use this information?

In this directory, the one you're in right now, are several subdirectories. They represent the varying stages of completeness of the project. They are redundant and build on each other, and each directory contains a ```README.md``` that tells you why it's there and what it does. You can follow just the instructions in order if you'd like to follow along, or you can just reverse-engineer the last stage in order to figure out what was done. Either way, it shouldn't be too terrible to follow (minus my awful humor), and I hope you enjoy!

-----


Best,

potc