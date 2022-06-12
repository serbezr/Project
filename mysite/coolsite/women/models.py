from django.db import models
from django.forms import DateTimeField

Class Women(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField(blank =True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField (auto_now =True)
    time_update = models.DateTimeField (auto_now =True)
    is_published = models.BooleanField (default =True)


