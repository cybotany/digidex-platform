from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from apps.chatbot.models import ChatMessage


class ChatbotAPIView(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Define the system template for the chatbot
        self.system_template = "You are an experienced head grower at an agritech consulting company assisting a(n) {user_experience}-{user_role}."
        self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)
    
        # Define the human template for the chatbot
        self.human_template = "{user_input}"
        self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template)

        # Define the chat prompt
        self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, self.human_message_prompt])

        # Defin the chat memory for the user
        self.chat_memory = ConversationBufferWindowMemory(return_messages=True, k=2)

        # Initialize LangChain
        self.conversation = ConversationChain(
            llm=ChatOpenAI(temperature=0, openai_api_key=config('OPENAI_API_KEY')),
            prompt=self.chat_prompt,
            verbose=True,
            memory=self.chat_memory
            )
        
        self.conversation.run(user_experience="Beginner", user_role="Houseplant Hobbyist", user_input="How many plants exist?")

    def post(self, request, *args, **kwargs):
        message = request.data.get('message')
        user = request.user

        # Input validation
        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve conversation history
        history = ChatMessage.objects.filter(user=user).order_by('created_at')
        history_text = '\n'.join([msg.content for msg in history])

        try:
            # Use LangChain to handle the conversation
            output = self.chatgpt_chain.predict(history=history_text, human_input=message)
        except Exception as e:
            # You might want to log the exception here
            return Response({"error": f"Failed to process your request due to {e}. Please try again later."},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # Save user input and AI's response to the database
        ChatMessage.objects.create(user=user, content=f'Human: {message}')
        ChatMessage.objects.create(user=user, content=f'Assistant: {output}')

        # Send the assistant's message back to the front-end
        return Response({'message': output})
