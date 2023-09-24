from decouple import config
from django.db import transaction
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from apps.chatbot.models import ChatMessage


class ChatService:
    def __init__(self):

        self.llm = OpenAI(
            temperature=0.0,
            openai_api_key=config('OPENAI_API_KEY')
        )
        self.conversation = ConversationChain(
            llm=self.llm
        )

    def converse(self, message):
        return self.conversation.predict(input=message)

    @staticmethod
    @transaction.atomic
    def save_message(user, message):
        chat_message = ChatMessage(
            user=user,
            content=message,
        )
        chat_message.save()
