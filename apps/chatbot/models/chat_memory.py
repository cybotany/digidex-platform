from langchain.memory import PostgresChatMessageHistory
from django.contrib.auth import get_user_model


class ChatMessage(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
