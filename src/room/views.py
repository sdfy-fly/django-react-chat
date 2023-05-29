from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.viewsets import ModelViewSet

from src.service.models import User
from .models import Room, RoomMembers
from .serializers import (RoomSerializers, RoomMembersSerializer, RoomMembersWriteSerializer)


class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

    # TODO: раскоментить
    # permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        queryset = self.__get_user_rooms(request)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # TODO: Добавить условие, что сменить название может только админ
        if self.get_object() in self.__get_user_rooms(request):
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):

        # Создание комнаты
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # При создании комнаты, юзер сразу становится ее членом и создателем
        room_member_serializer = RoomMembersWriteSerializer(data={
            "room": serializer.data["id"],
            "user": request.user.id,
            "role": 1,
        })
        room_member_serializer.is_valid(raise_exception=True)
        room_member_serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        # TODO: Добавить условие, что удалить чат может только админ, если чденов комнаты > 2
        if self.get_object() in self.__get_user_rooms(request):
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def __get_user_rooms(request):
        return [x.room for x in User.objects.get(id=1).rooms.all()]
        # TODO: раскоментить
        # return [x.room for x in User.objects.get(id=request.user).rooms.all()]


class RoomMembersView(ModelViewSet):
    queryset = RoomMembers.objects.all()
    serializer_class = RoomMembersSerializer

    # TODO: раскоментить
    # permission_classes = [permissions.IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action == 'create':
            return RoomMembersWriteSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):

        room_id = request.data.get("room_id")
        user_id = request.data.get("user_id")

        if not room_id:
            return Response({"detail": "Room id is required!"}, status=status.HTTP_400_BAD_REQUEST)

        if not user_id:
            return Response({"detail": "User id is required!"}, status=status.HTTP_400_BAD_REQUEST)

        # Если юзера нет в этой комнате
        if request.user not in [x.user for x in RoomMembers.objects.filter(room__id=room_id)]:
            return Response({"detail": "Invalid permission for this message!"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        room_id = kwargs["pk"]
        members = RoomMembers.objects.filter(room__pk=room_id)
        serializer = self.get_serializer(members, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # TODO: УДАЛЯТЬ ЮЗЕРОВ МОЖЕТ ТОЛЬКО АДМИНИСТРАТОР
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # вернуть ошибку
        return super().update(request, *args, **kwargs)
