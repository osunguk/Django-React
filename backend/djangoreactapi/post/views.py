#backend/post/views.py
from django.shortcuts import render, redirect
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def home(request):
    return render(request, 'app/home.html')


def auth(request):
    
    return redirect('home')