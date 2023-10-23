from django.conf import settings
from langchain.llms import OpenAI
from langchain.chains import ConversationChain


class ChatService:
    def __init__(self):
        self.llm = OpenAI(
            temperature=0.0,
            openai_api_key=settings.OPENAI_API_KEY,  # Reading the API key from Django settings
            model_name='gpt-3.5-turbo',
        )
        self.conversation = ConversationChain(
            llm=self.llm
        )

    def converse(self, message):
        return self.conversation.predict(input=message)
