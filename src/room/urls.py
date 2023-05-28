from rest_framework import routers
from django.urls import path, include

from .views import RoomView, MessageView


router = routers.SimpleRouter()

router.register('chat', RoomView)
router.register('message', MessageView)


urlpatterns = [
    path('', include(router.urls))
]