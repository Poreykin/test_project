from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User, db_index=True, null=False, blank=False, on_delete=models.CASCADE)

    name = models.CharField(max_length=128, unique=True, db_index=True, null=False, blank=False)
    text = models.TextField(db_index=False, null=False, blank=True)

    added_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
