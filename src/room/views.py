from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.viewsets import ModelViewSet

from .models import Room, Message
from .serializers import (RoomSerializers, ChatSerializers)
from src.service.models import User


# api/chat    get    - получение всех чатов у юзера с id 1
# api/chat    post   - создание чата
# api/chat/1/ put    - смена названия чата
# api/chat/1/ delete - удаление чата

# api/chat/message/1 retrive - получить все сообщения комнаты 1
# api/chat/message/1 put - отредактировать сообщение юзера в комнате 1
# api/chat/message/1 post - добавить сообщение юзера в комнату 1
# api/chat/message/1 delete - удалить сообщение юзера в комнате 1

# api/chat/members/1 retrieve - получить всех юзеров комнаты 1
# api/chat/members post   - добавить юзера в комнату
# api/chat/members delete - удалить юзера из комнаты

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
        if self.get_object() in self.__get_user_rooms(request):
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if self.get_object() in self.__get_user_rooms(request):
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def __get_user_rooms(request):
        return [x.room for x in User.objects.get(id=1).rooms.all()]
        # TODO: раскоментить
        # return [x.room for x in User.objects.get(id=request.user).rooms.all()]

