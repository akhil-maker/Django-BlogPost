from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView
from rest_framework import permissions
from .models import Posts, Contact
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import PostsSerializer, ContactSerializer


# Create your views here.

class PostListView(generics.ListAPIView):
    serializer_class = PostsSerializer
    pagination_class = PageNumberPagination
    queryset = Posts.objects.all()

class PostDetailView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class ContactListView(generics.ListAPIView):
    pagination_class = PageNumberPagination
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CreateContactView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()

class PostsCreateView(UserPassesTestMixin, generics.CreateAPIView):
    serializer_class = PostsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def test_func(self):
        return self.request.user.is_active

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostsDeleteView(UserPassesTestMixin, generics.DestroyAPIView):
    def get_queryset(self):
        if self.request.user.is_active:
            username = self.request.user.username
        queryset = Posts.objects.filter(writer=username)
        return queryset

    permission_classes = (permissions.IsAuthenticated,)

    def test_func(self):
        return self.request.user.is_active

    def perform_destroy(self, instance):
        instance.delete()

class PostUpdateView(UserPassesTestMixin, generics.UpdateAPIView):
    serializer_class = PostsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def test_func(self):
        return self.request.user.is_active

    def get_queryset(self):
        if self.request.user.is_active:
            username = self.request.user.username
        queryset = Posts.objects.filter(writer=username)
        return queryset

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class AuthView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        content = {'message': 'You are authenticated, Save your Token!'}
        return Response(status=status.HTTP_200_OK)


"""
import smtplib

GMAIL_ID = 'abc@gmail.com'
GMAIL_PSWD = 'xyz'
def sendEmail(to, sub, msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject{sub} and {msg}")
    s.quit()

if __name__ == "__main__":
    sendEmail(GMAIL_ID, "subject", "Hello")
    exit()
    
"""