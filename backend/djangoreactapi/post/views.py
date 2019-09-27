#backend/post/views.py
from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


def home(request):
    return render(request, 'app/home.html')


def auth(request):
    code = request.GET.get('code')
    client_id = '2164b8cf12e0e79b610070b46396fc28'
    redirect_uri = 'http://127.0.0.1:8000/auth/'

    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'code': code
    }
    response = requests.post('https://kauth.kakao.com/oauth/token', data=data)
    response_json = response.json()
    headers = {
        'Authorization': 'Bearer {}'.format(response_json['access_token']),
        }

    response2 = requests.get('https://kapi.kakao.com/v2/user/me', headers=headers)
    response2_json = response2.json()

    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(response2_json)

    username = str(response2_json['properties']['nickname'])+'#'+str(response2_json['id'])
    if (User.objects.filter(username=username).exists() == False):
        u = User.objects.create_user(
            username=username,
            password='',
            last_login=timezone.localtime(),
            is_staff=False,
        )
        profile = Profile(user=u, type='kakao', image=response2_json['properties']['profile_image'])
        profile.save()

    return redirect('http://localhost:3000/')
