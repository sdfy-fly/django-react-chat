from django.urls import path, include
from rest_framework import routers

from .views import MessageView


router = routers.SimpleRouter()

router.register('message', MessageView)


urlpatterns = [
    path('', include(router.urls))
]