from rest_framework import serializers

from src.service.models import User
from .models import Room, Message


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "full_name", "email", "image_link")


class RoomSerializers(serializers.ModelSerializer):
    """Сериализация чата"""

    class Meta:
        model = Room
        fields = ("id", "name")


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


class MessageSerializer(serializers.ModelSerializer):
    room = RoomSerializers(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'room', 'user', 'text', 'created_at', 'updated_at')


class MessageWriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    class Meta:
        model = Message
        fields = '__all__'
