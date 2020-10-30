from django.contrib import admin
from .models import Posts, Contact
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Posts)
admin.site.register(Contact)