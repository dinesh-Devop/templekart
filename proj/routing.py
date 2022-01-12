from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app.consumers import EventConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/", EventConsumer.as_asgi()),
    ])
})
