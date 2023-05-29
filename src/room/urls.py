from rest_framework import routers
from django.urls import path, include

from .views import RoomView, RoomMembersView

router = routers.SimpleRouter()

router.register('chat/members', RoomMembersView, basename='chat/members')
router.register('chat', RoomView)


urlpatterns = [
    path('', include(router.urls))
]