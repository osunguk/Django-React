#backend/post/serializers.py
from rest_framework import serializers
from .models import Post
from . import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
        )
        model = Post


class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)
    class Meta:
        model = models.User
        fields = ('id', 'email', 'username', 'image')
