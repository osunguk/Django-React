#backend/post/serializers.py
from rest_framework import serializers
from .models import Post, Profile
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
    class Meta:
        model = models.User
        fields = (
            'id',
            'username',
            'email',
            )


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedRelatedField(view_name='test', read_only=True)
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = (
            'id',
            'type',
            'image',
            'memo',
            'user',
            )



