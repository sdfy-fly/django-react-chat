from rest_framework import serializers

from .models import Room, RoomMembers
from src.service.models import User, UserRoomGroup
from src.service.serializers import UserSerializer, UserRoomGroupSerializer


class RoomSerializers(serializers.ModelSerializer):
    """Сериализация чата"""

    class Meta:
        model = Room
        fields = ("id", "name")


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
    role = serializers.PrimaryKeyRelatedField(queryset=UserRoomGroup.objects.all())

    class Meta:
        model = RoomMembers
        fields = ('room', 'user', 'role')
