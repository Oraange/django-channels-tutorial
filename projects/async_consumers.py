import json
import time
from asgiref.sync import async_to_sync

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Project


@receiver(post_save, sender=Project)
def send_state(sender, instance, created, **kwargs):
    if not created:
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)("share", {"type": "change_state", "state": instance.state})


class ProjectConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.user = self.scope["user"]
        self.group_name = "share"
        self.user = self.scope["user"]

        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # 여기선 사용 X
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        state = text_data_json["state"]

        await self.channel_layer.group_send(
            self.group_name, {"type": "change_state", "state": state}
        )

    async def change_state(self, event):
        state = event["state"]
        print(f"State: {state}")
        print(self.user)

        await self.send(text_data=json.dumps({"state": state}))
