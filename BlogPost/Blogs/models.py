from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField(unique=True, max_length=100)
    content = models.CharField(max_length=120)
    tagline = models.TextField(max_length=120)
    date = models.DateTimeField(max_length=12, auto_now_add=True) #Date and time will be add automatically by django

    def __str__(self):
        return self.title
