from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=30)
    writer = models.CharField(max_length=100)
    content = models.TextField(max_length=150)
    tagline = models.CharField(max_length=120)
    date = models.DateTimeField(max_length=12, auto_now_add=True)  #Date and time will be add automatically by django
    img = models.ImageField(null=True, max_length=100)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    msg = models.TextField(max_length=100)
    date = models.DateTimeField(max_length=12, auto_now_add=True)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

