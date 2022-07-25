# from django.db import models
# from django.contrib.auth.models import User

# class Room(models.Model):
#     """Модель комнаты чата"""
#     creator = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE)
#     invited = models.ManyToManyField(User, verbose_name="Участники", related_name="invited_user")
#     date = models.DateTimeField("Дата создания", auto_now_add=True)

#     class Meta:
#         verbose_name = "Комната чата"
#         verbose_name_plural = "Комнаты чатов"


# class Chat(models.Model):
#     """Модель чата"""
#     room = models.ForeignKey(Room, verbose_name="Комната чата", on_delete=models.CASCADE)
#     user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
#     text = models.TextField("Сообщение", max_length=500)
#     date = models.DateTimeField("Дата отправки", auto_now_add=True)

#     class Meta:
#         verbose_name = "Сообщение чата"
#         verbose_name_plural = "Сообщения чатов"

from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self) :
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    