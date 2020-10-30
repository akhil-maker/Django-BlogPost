from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.contrib.auth.models import User
from .views import *

urlpatterns = [
    path("create/", views.PostsCreateView.as_view(), name='create'),
    path('createcontact/', views.CreateContactView.as_view(), name='create_contact'),
    path('contact/', ContactListView.as_view()),
    path("", PostListView.as_view(), name="index"),
    path("<int:pk>/detail/", PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', PostsDeleteView.as_view(), name='delete'),
    path('auth/', views.AuthView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_auth_token'),
]