from django.urls import re_path

from web.views import *

urlpatterns = [
    re_path('', index),
]

