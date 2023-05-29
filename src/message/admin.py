from django.contrib import admin

from .models import Message


@admin.register(Message)
class ChatAdmin(admin.ModelAdmin):
    """Сообщения"""
    list_display = ("id", "room", "user", "text", "created_at", "updated_at")
