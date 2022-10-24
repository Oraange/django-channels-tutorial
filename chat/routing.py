from django.urls import re_path

from . import async_consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", async_consumers.ChatConsumer.as_asgi()),
]
