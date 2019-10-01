#backend/post/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, default='tmp', null=True, blank=True)
    image = models.ImageField(default='luis-rocha-yM_mQIl5Vks-unsplash.jpg',blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)
