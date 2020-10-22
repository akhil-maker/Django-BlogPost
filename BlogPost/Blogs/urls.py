from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="Blogs"),
    #path("addnew/<int:id>/", views.newtitle, name="Edit"),
    path('add/<int:id>/', views.add, name='Post'),
]