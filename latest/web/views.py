from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from web.models import *

import requests as r

# Create your views here.
def index(request):
    return render(request, 'index.html')

def posts(request, post_type):
    context = dict()
    context['posts'] = list()

    if post_type == 'geeky':
        # use a cool API to grab a bunch of geeky quotes
        # this one is a bit expensive due to the API's design
        for _ in range(10):
            resp = r.get('https://geek-jokes.sameerkumar.website/api')
            context['posts'].append(resp.text.strip())

    else:
        # use this super friendly API to grab 10 lorem ipsums
        resp = r.get('https://loripsum.net/api/10/long/plaintext')

        # split those into their respective parts
        context['posts'] = [el.strip() for el in resp.text.splitlines() if el]

    return render(request, 'posts.html', context=context)

def favorites(request):
    context = dict()

    # grab all of the favorite objects from our database
    context['favorites'] = Favorite.objects.all().order_by('-likes')

    return render(request, 'favorites.html', context=context)

def like_favorite(request, id):
    try: 
        if request.method == 'GET':
            liked_fav = Favorite.objects.filter(id=id)
            
            if not liked_fav:
                raise NotImplementedError
            else:
                liked_fav[0].likes += 1
                liked_fav[0].save(update_fields=['likes'])
    
            return JsonResponse({'data': True})
        else:
            return JsonResponse({'data': False})
    except:
        return JsonResponse({'data': False})

def add_favorite(request, quote):
    try: 
        if request.method == 'GET':
            new_fav = Favorite.objects.create(
                body=quote
            )
            new_fav.save()
            return JsonResponse({'data': True})
        else:
            return JsonResponse({'data': False})
    except:
        return JsonResponse({'data': False})