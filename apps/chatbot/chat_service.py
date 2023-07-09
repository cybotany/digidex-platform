from decouple import config
from django.db import transaction
from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.prompt import PromptTemplate

from apps.chatbot.models import ChatMessage
from apps.utils.constants import CHAT_TEMPLATE


class ChatService:
    def __init__(self):

        self.prompt = PromptTemplate(input_variables=['history', 'input'], template=CHAT_TEMPLATE)
        self.llm = OpenAI(temperature=0.0, openai_api_key=config('OPENAI_API_KEY'))
        self.memory = ConversationBufferMemory(memory_key='history', ai_prefix="AI Assistant")

        self.conversation = ConversationChain(
            llm=self.llm,
            prompt=self.prompt,
            verbose=True,
            memory=self.memory
        )

    def converse(self, message):
        return self.conversation.predict(input=message)

    @staticmethod
    @transaction.atomic
    def save_message(session_id, user, message):
        chat_message = ChatMessage(
            session_id=session_id,
            user=user,
            message=message,
        )
        chat_message.save()
