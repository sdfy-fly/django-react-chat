# import os
# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')

# application = get_asgi_application()
# "websocket": AuthMiddlewareStack(
#    URLRouter(room.routing.websocket_urlpatterns)
# ),

import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing
from room.chatmiddleware import TokenAuthMiddleware


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': TokenAuthMiddleware(
        URLRouter(room.routing.websocket_urlpatterns)
    ),
})
