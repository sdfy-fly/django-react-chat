from src.service.models import User, UserRoomGroup
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RoomMembers(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rooms")
    role = models.ForeignKey(UserRoomGroup, on_delete=models.DO_NOTHING, default=3, related_name="roles")
