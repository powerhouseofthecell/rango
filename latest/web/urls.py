from django.urls import re_path, path

from web.views import *

urlpatterns = [
    path('posts/<str:post_type>', posts),
    path('favorites', favorites),
    path('like_favorite/<int:id>', like_favorite),
    path('add_favorite/<str:quote>', add_favorite),
    re_path('', index),
]

