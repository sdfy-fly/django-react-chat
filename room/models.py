from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    first_user = models.CharField(max_length=255, blank=True)
    second_user = models.CharField(max_length=255, blank=True)

    def __str__(self) :
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    