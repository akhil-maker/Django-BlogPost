from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('edit/<int:id>/', views.PostUpdateView.as_view(), name='edit'),
    path('add/<int:id>/', views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),

]