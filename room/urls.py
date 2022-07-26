from django.urls import path 
from .views import *

urlpatterns = [
    path('room/', Rooms.as_view()),
    path('dialog/', Dialog.as_view()),
    path('signup/', CreateUser.as_view()),
]