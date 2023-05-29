from rest_framework import serializers

from .models import Message

from src.room.serializers import RoomSerializers
from src.room.models import Room

from src.service.serializers import UserSerializer
from src.service.models import User


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
