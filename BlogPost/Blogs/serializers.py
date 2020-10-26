from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Posts, Contact

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'title', 'tagline', 'writer', 'content', 'date', 'img')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        field = ('id', 'name', 'phone', 'msg', 'date', 'email')

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=5, write_only=True)

    def create(self, validated_data):  # we have to use create_user method from User class as we are creating a new User using builtin authentication system, so regular create method won't work
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

