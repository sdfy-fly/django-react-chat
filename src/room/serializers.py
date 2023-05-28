from rest_framework import serializers

from src.service.models import User
from .models import Room, Message, RoomMembers
from src.service.serializers import UserSerializer, UserRoomGroupSerializer


class RoomSerializers(serializers.ModelSerializer):
    """Сериализация чата"""

    class Meta:
        model = Room
        fields = ("id", "name")


class MessageSerializer(serializers.ModelSerializer):
    room = RoomSerializers(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'room', 'user', 'text', 'is_edited', 'created_at', 'updated_at')


class MessageWriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    class Meta:
        model = Message
        fields = '__all__'


class RoomMembersSerializer(serializers.ModelSerializer):
    room = RoomSerializers(read_only=True)
    user = UserSerializer(read_only=True)
    role = UserRoomGroupSerializer(read_only=True)

    class Meta:
        model = RoomMembers
        fields = ('room', 'user', 'role')


class RoomMembersWriteSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = RoomMembers
        fields = ('room', 'user')
