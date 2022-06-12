from django.urls import re_path
from .view import*


urlpatterns=[
    path(' ',index),
    path('cats',categories),
]