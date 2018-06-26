import os
from django.db import models
from django.contrib.auth.models import User
from test1.settings import MEDIA_ROOT

class Photo(models.Model):
    uploader = models.ForeignKey(User, db_index=True, null=False, blank=False, on_delete=models.CASCADE)

    image_file = models.ImageField(upload_to='photos', unique=True)
    
    added_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
