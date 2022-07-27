from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import User

from .models import Room, Message
from .serializers import (RoomSerializers, ChatSerializers)


class Rooms(APIView):
    """Комнаты чата"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self,request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})

class Dialog(APIView):
    """Диалог чата, сообщение"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        room = request.GET.get("room")
        chat = Message.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

class CreateUser(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self,request) : 

        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        
        if User.objects.filter(username=username).exists():
            return Response(status=400)
        if User.objects.filter(email=email).exists():
            return Response(status=400)
         
        user = User.objects.create_user(username=username , password=password , email=email)
        user.save()
        return Response(status=201)

