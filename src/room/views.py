from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.viewsets import ModelViewSet

from .models import Room, Message
from .serializers import (RoomSerializers, MessageSerializer, MessageWriteSerializer)
from src.service.models import User


# api/chat    get    - получение всех чатов у юзера
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


class MessageView(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # TODO: раскоментить
    # permission_classes = [permissions.IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action == 'create':
            return MessageWriteSerializer
        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        """
            Метод для получения всех сообщений в определенной комнате по id
        """
        try:
            room = Room.objects.get(pk=kwargs["pk"])
        except Room.DoesNotExist:
            return Response({"detail": "Invalid room pk!"}, status=status.HTTP_400_BAD_REQUEST)

        messages = Message.objects.filter(room=room)
        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
            Метод для создания сообщения
            Принимает: room (room_id) int, user (user_id) int, text (message text) string
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
            Метод для обновления текста сообщения по его id
            Если владелец сообщения != request.user - возвращаю статус 400
        """

        if self.get_object().user != request.user:
            return Response({"detail": "Invalid permission for this message!"}, status=status.HTTP_400_BAD_REQUEST)

        if not request.data.get('text'):
            return Response({"detail": "Text message is required!"}, status=status.HTTP_400_BAD_REQUEST)

        message_text = request.data.get('text')
        instance = self.get_object()
        instance.is_edited = True
        instance.text = message_text

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
            Метод для удаления сообщения по его id
            Если владелец сообщения != request.user - возвращаю статус 400
        """
        if self.get_object().user == request.user:
            return super().destroy(request, *args, **kwargs)
        return Response({"detail": "Invalid message pk!"}, status=status.HTTP_400_BAD_REQUEST)
