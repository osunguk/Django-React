#backend/djangoreactapi/urls.py
from django.contrib import admin
from django.urls import path, include
import post.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('post.urls')),
    path('', post.views.home, name='home'),
]