from django.db import models
from . import ChatMessage


class ChatHistory(models.Model):
    def add_user_message(self, message, **kwargs):
        ChatMessage.objects.create(
            message_type='H',
            content=message,
            additional_kwargs=kwargs,
        )

    def add_ai_message(self, message, **kwargs):
        ChatMessage.objects.create(
            message_type='A',
            content=message,
            additional_kwargs=kwargs,
        )
