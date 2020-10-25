from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path("create/", views.PostsCreateView.as_view(), name='create'),
    path("", PostListView.as_view(), name="index"),
    path("<int:pk>/detail/", PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', PostsDeleteView.as_view(), name='delete'),
]