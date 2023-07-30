import json
import traceback

# from django.core.checks import messages
from channels.generic.websocket import AsyncWebsocketConsumer
# from django.contrib.contenttypes.models import ContentType
from channels.db import database_sync_to_async

from apps.notification.models import Notification


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name ="1"
        self.room_group_name = "notify_1"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        raise NotImplementedError()
    async def send_notification(self, event):

        message = event['message']
        await self.send(
            text_data=json.dumps({
                'notification': message,
            })
        )

