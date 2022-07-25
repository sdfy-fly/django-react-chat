from django.contrib import admin
from .models import Room, Message


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("name",)

    # def invited_user(self, obj):
    #     return "\n".join([user.username for user in obj.invited.all()])


@admin.register(Message)
class ChatAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("room", "user", "text", "date_added")