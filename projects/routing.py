from django.urls import re_path

from . import async_consumers

websocket_urlpatterns = [
    re_path(r"ws/projects/$", async_consumers.ProjectConsumer.as_asgi()),
]
