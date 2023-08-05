from decouple import config
from django.db import transaction
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory, ConversationBufferMemory, ChatMessageHistory
from langchain.prompts.prompt import PromptTemplate

from apps.chatbot.models import ChatMessage
from apps.utils.constants import CHAT_TEMPLATE


class ChatService:
    def __init__(self):

        self.prompt = PromptTemplate(input_variables=['chat_history', 'human_input'], template=CHAT_TEMPLATE)
        self.llm = OpenAI(temperature=0.0, openai_api_key=config('OPENAI_API_KEY'))

        # Load user-specific chat history to provide context
        self.message_history = ''#ChatHistory()

        self.memory = ConversationBufferMemory(
            ai_prefix='AI Assistant',
            chat_memory=self.message_history,
            memory_key='chat_history'
        )

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
    def save_message(user, message):
        chat_message = ChatMessage(
            user=user,
            content=message,
        )
        chat_message.save()
