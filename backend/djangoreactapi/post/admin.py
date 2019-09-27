#backend/post/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Post, Profile
from django.contrib.auth.models import User, Group


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = '프로필'
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ['username', 'email', 'type']

    def type(self, obj):
        return Profile.objects.get(user=obj).type


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post)