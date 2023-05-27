from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import User

from .models import Room, Message
from .serializers import (RoomSerializers, ChatSerializers)


class Rooms(APIView): 
    """
    Диалоги чата: Get запрос возвращает список всех комнат
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self,request):
        username = request.GET.get('username')
        rooms = Room.objects.filter(Q(first_user = username) | Q(second_user = username))
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})

    def post(self,request) : 
        first_user = request.POST.get('first_user')
        second_user = request.POST.get('second_user')
        name = f'{first_user}-{second_user}'

        room = Room.objects.create(name=name, first_user=first_user, second_user=second_user)
        room.save()
        return Response(status=200)


class Dialog(APIView):
    """Получение сообщений из определенного диалога"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        room = request.GET.get("room")

        try:  
            id = Room.objects.get(name = room).pk
        except : 
            return Response({"error" : "wrong room name"})

        chat = Message.objects.filter(room=id)
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
        return Response(status=200)

