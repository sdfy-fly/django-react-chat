from rest_framework import routers
from django.urls import path, include

from .views import RoomView


router = routers.SimpleRouter()
router.register('chat', RoomView)

urlpatterns = [
    path('', include(router.urls))
]