from django.urls import re_path

from rango.web.views import *

urlpatterns = [
    re_path('', index),
]

