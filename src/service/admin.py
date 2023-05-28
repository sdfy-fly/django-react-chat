from django.contrib import admin

from .models import User, UserRoomGroup


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'password')


@admin.register(UserRoomGroup)
class UserRoomGroupAdmin(admin.ModelAdmin):
    pass
