from django.db import models
from apps.utils.constants import MESSAGE_TYPES


class ChatMessage(models.Model):
    session = models.ForeignKey('ChatSession', on_delete=models.CASCADE, related_name='messages')
    message_type = models.CharField(max_length=1, choices=MESSAGE_TYPES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    additional_kwargs = models.JSONField(default=dict)

    class Meta:
        ordering = ['timestamp']
