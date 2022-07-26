from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Room, Message


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):
    """Сериализация комнат чата"""
    class Meta:
        model = Room
        fields = ("id", "name" , "slug")


class ChatSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    user = UserSerializer()
    class Meta:
        model = Message
        fields = ("user", "text", "date_added")


class ChatPostSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    class Meta:
        model = Message
        fields = ("room", "text")