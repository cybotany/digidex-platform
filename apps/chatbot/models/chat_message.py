from django.db import models


class ChatMessage(models.Model):
    session_id = models.TextField()
    message = models.JSONField()

    class Meta:
        ordering = ['id']
