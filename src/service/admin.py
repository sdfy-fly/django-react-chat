from django.contrib import admin

from .models import User


@admin.register(User)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'password')
