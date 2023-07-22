from django.db import models
from django.utils import timezone
from .chat_message import ChatMessage


class ChatSession(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    summary = models.TextField(blank=True, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='sessions')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)

    def add_user_message(self, message, **kwargs):
        ChatMessage.objects.create(
            session=self,
            message_type='H',
            content=message,
            additional_kwargs=kwargs,
        )

    def add_ai_message(self, message, **kwargs):
        ChatMessage.objects.create(
            session=self,
            message_type='A',
            content=message,
            additional_kwargs=kwargs,
        )

    def add_agent_message(self, message, **kwargs):
        ChatMessage.objects.create(
            session=self,
            message_type='G',
            content=message,
            additional_kwargs=kwargs,
        )

    def end_session(self):
        self.end_time = timezone.now()
        self.is_active = False
        self.save()

    def get_chat_history(self):
        return self.messages.order_by('timestamp')

    def generate_summary(self):
        # Implement the logic for generating a conversation summary here.
        # You can make use of the `ConversationSummaryBufferMemory` in the langchain library,
        # or write your own summarization logic.
        pass
