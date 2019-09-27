#backend/post/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPost.as_view()),
    path('<int:pk>/', views.DetailPost.as_view()),
    path('users/', views.UserListView.as_view()),
]