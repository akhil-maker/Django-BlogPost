from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from rest_framework import permissions
from .models import Posts
from django.views import generic
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostsSerializer, UserSerializer
# Create your views here.

class PostListView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class PostsCreateView(generics.CreateAPIView):
    serializer_class = PostsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostsDeleteView(generics.DestroyAPIView):
    queryset = Posts.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_destroy(self, instance):
        instance.delete(user=self.request.user)

class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_update(self, serializer):
        current_user = self.request.user
        user = self.request.user
        if user:
            serializer.save(user=self.request.user)

class AuthView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        content = {'message': 'You are authenticated, Save your Token!'}
        return Response(status=status.HTTP_200_OK)
