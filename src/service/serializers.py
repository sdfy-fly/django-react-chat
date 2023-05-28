from rest_framework import serializers

from .models import User, UserRoomGroup


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "full_name", "email", "image_link")


class UserRoomGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoomGroup
        fields = '__all__'
