from django.db import models


class ChatSession(models.Model):
    session_id = models.TextField(unique=True)

    def get_chat_history(self):
        return "\n".join([
            f"{message.timestamp} {message.user}: {message.message}"
            for message in self.messages.all().order_by('timestamp')
        ])
