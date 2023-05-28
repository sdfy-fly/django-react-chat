from src.service.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RoomMembers(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="rooms")


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.DO_NOTHING)
    text = models.TextField()
    is_edited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
