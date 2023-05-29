from django.contrib import admin
from .models import Room, RoomMembers


class RoomMembersInline(admin.TabularInline):
    model = RoomMembers


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomMembersInline]


@admin.register(RoomMembers)
class RoomMembersAdmin(admin.ModelAdmin):
    pass
