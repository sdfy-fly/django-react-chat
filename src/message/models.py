from django.db import models

from src.room.models import Room
from src.service.models import User


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.DO_NOTHING)
    text = models.TextField()
    is_edited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
