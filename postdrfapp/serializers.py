from django.db.models import fields
from rest_framework import serializers
from .models import *

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'gender', 'email', 'password']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"

class PostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = "__all__"