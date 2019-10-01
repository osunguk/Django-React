#backend/post/views.py
from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, ProfileSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
from django.contrib.auth.models import User
from .models import Profile, models
from . import serializers
from django.utils import timezone


class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserListView(generics.ListAPIView):
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ProfileListView(generics.ListAPIView):
    permission_classes = ()
    queryset = Profile.objects.all()
    serializer_class =  serializers.ProfileSerializer


class ProfileDetailView(generics.RetrieveAPIView):
    permission_classes = ()
    queryset = Profile.objects.all()
    serializer_class =  serializers.ProfileSerializer

def home(request):
    return render(request, 'app/home.html')


def auth(request):
    code = request.GET.get('code')
    client_id = '2164b8cf12e0e79b610070b46396fc28'
    redirect_uri = 'http://127.0.0.1:8000/auth/'
    #redirect_uri = 'http://localhost:3000'

    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'code': code
    }
    response = requests.post('https://kauth.kakao.com/oauth/token', data=data)
    response_json = response.json()
    print('response_json',response_json)
    headers = {
        'Authorization': 'Bearer {}'.format(response_json['access_token']),
        }

    response2 = requests.get('https://kapi.kakao.com/v2/user/me', headers=headers)
    response2_json = response2.json()
    print('response2_json', response2_json)
    username = str(response2_json['properties']['nickname'])+'@'+str(response2_json['id'])
    if not User.objects.filter(username=username).exists():
        u = User.objects.create_user(
            username=username,
            password='',
            last_login=timezone.localtime(),
            is_staff=False,
        )
        if 'profile_image' in response2_json['properties'].keys():
            profile = Profile(user=u, type='kakao', memo=response_json)
            print('working')
        else:
            profile = Profile(user=u, type='kakao', image=response2_json['properties']['profile_image'], memo=response_json)
        profile.save()

        test = 'test'

    return render(request, 'app/home.html')