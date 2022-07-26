from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import User

from .models import Room, Message
from .serializers import (RoomSerializers, ChatSerializers, ChatPostSerializers,  UserSerializer)


class Rooms(APIView):
    """Комнаты чата"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self,request):
        # rooms = Room.objects.filter(Q(creator=request.user) | Q(invited=request.user))
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})

    # def post(self, request):
    #     Room.objects.create(creator=request.user)
    #     return Response(status=201)


class Dialog(APIView):
    """Диалог чата, сообщение"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        room = request.GET.get("room")
        chat = Message.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

    # def post(self, request):
        # room = request.data.get("room")
        # dialog = ChatPostSerializers(data=request.data)
        # if dialog.is_valid():
        #     dialog.save(user=request.user)
        #     return Response(status=201)
        # else:
        #     return Response(status=400)

class CreateUser(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self,request) : 

        username = request.data.get("username")
        password = request.data.get("password")
        
        if User.objects.filter(username=username).exists():
            return Response(status=401)
         
        user = User.objects.create_user(username=username , password=password)
        user.save()
        return Response(status=201)


# class AddUsersRoom(APIView):
#     """Добавление юзеров в комнату чата"""
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         room = request.data.get("room")
#         user = request.data.get("user")
#         try:
#             room = Room.objects.get(id=room)
#             room.invited.add(user)
#             room.save()
#             return Response(status=201)
#         except:
#             return Response(status=400)