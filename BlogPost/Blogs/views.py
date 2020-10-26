from django.shortcuts import render, HttpResponse
from django.views.generic import UpdateView, ListView, View
from .models import Posts
from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostsSerializer, UserSerializer
from django.contrib.auth import login, authenticate
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

class SignupView(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        content = {'message':'You are authenticated, Save your Token!'}
        return Response(status=status.HTTP_200_OK)