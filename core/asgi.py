import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

import src.room.routing
from src.room import TokenAuthMiddleware


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': TokenAuthMiddleware(
        URLRouter(src.room.routing.websocket_urlpatterns)
    ),
})
