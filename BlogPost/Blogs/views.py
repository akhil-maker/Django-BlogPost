from django.shortcuts import render, HttpResponse
from django.views.generic import UpdateView, ListView
from .models import Posts
from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.utils import timezone
from rest_framework import generics
from .serializers import PostsSerializer
from django.contrib.auth.models import User
# Create your views here.

class PostListView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class PostsCreateView(generics.CreateAPIView):
    serializer_class = PostsSerializer

class PostsDeleteView(generics.DestroyAPIView):
    queryset = Posts.objects.all()

class PostUpdateView(generics.UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


