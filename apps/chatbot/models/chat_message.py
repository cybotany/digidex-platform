from django.db import models


class ChatMessage(models.Model):
    user = models.TextField(default='AI')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
