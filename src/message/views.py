from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Message
from .serializers import MessageSerializer, MessageWriteSerializer
from src.room.models import Room


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
