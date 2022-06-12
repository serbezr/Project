from django.urls import path, re_path
from .view import*


urlpatterns=[
    path(' ',index, name='home'),
    path('cats/<slag:cat>/', categories, name="cats")
    re-path(r'^archive/(?P<year>[0-9]{4}/, archive', name='archive'),
]