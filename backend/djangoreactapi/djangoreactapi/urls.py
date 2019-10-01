#backend/djangoreactapi/urls.py
from django.contrib import admin
from django.urls import path, include
import post.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('post.urls')),
    path('', post.views.home, name='home'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('auth/', post.views.auth, name='auth'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
