from django.shortcuts import render

import requests as r

# Create your views here.
def index(request):
    return render(request, 'index.html')

def posts(request):
    context = dict()

    # use this super friendly API to grab 10 lorem ipsums
    resp = r.get('https://loripsum.net/api/10/long/plaintext')

    # split those into their respective parts
    context['posts'] = [el.strip() for el in resp.text.splitlines() if el]

    return render(request, 'posts.html', context=context)