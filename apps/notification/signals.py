import channels.layers
from asgiref.sync import async_to_sync

from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.notification.models import Notification


@receiver(post_save, sender=Notification)
def notify_user_with_socket(sender, instance, created, **kwargs):
    if created:
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notify_1",
            {
                'type': 'send_notification',
                'message': instance.content
            }
        )