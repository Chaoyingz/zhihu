from django.contrib import admin

from .models import UserProfile


class UserProfileField(admin.ModelAdmin):
    fields = ('username', 'mobile', 'email', 'views', 'gender')


admin.site.register(UserProfile, UserProfileField)
