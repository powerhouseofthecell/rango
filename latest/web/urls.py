from django.urls import re_path, path

from web.views import *

urlpatterns = [
    path('posts/<str:post_type>', posts),
    path('add_favorite/<str:quote>', add_favorite),
    re_path('', index),
]

