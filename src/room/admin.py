from django.contrib import admin
from .models import Room, RoomMembers, Message


class RoomMembersInline(admin.TabularInline):
    model = RoomMembers


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomMembersInline]


@admin.register(RoomMembers)
class RoomMembersAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class ChatAdmin(admin.ModelAdmin):
    """Сообщения"""
    list_display = ("id", "room", "user", "text", "created_at", "updated_at")
