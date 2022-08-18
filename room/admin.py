from django.contrib import admin
from .models import Room, Message


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("id" , "name" , "first_user" , "second_user")


@admin.register(Message)
class ChatAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("room", "user", "text", "date_added")