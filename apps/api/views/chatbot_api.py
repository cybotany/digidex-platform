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

from apps.accounts.models import Profile
from apps.chatbot.models import ChatMessage


class ChatbotAPIView(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Define the chat memory for the user
        self.memory = ConversationBufferWindowMemory(return_messages=True, k=2)

        # Define the system template for the chatbot
        self.system_template = "You are an experienced head grower at an agritech consulting company assisting a(n) {user_interest} with a {user_experience}-level knowledge of the subject."
        self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)

        # Define the human template for the chatbot
        self.human_template = "{user_input}"
        self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template)

        # Define the chat prompt
        self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, self.human_message_prompt])

        # Initialize LangChain
        self.conversation = ConversationChain(
            llm=ChatOpenAI(temperature=0, openai_api_key=config('OPENAI_API_KEY')),
            prompt=self.chat_prompt,
            verbose=True,
            memory=self.memory
        )

    def post(self, request, *args, **kwargs):
        message = request.data.get('message')
        user = request.user

        # Input validation
        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch user's profile and info
        profile = Profile.objects.get(user=user)
        user_interest = profile.interests
        user_experience = profile.experience
        
        # Add interest and experience to the system prompt template
        self.chat_prompt.format_prompt(
            user_interest=user_interest,
            user_experience=user_experience
        )

        # Populate chat memory with historical chat messages
        chat_history = ChatMessage.objects.filter(user=user).order_by('-created_at')
        for msg in chat_history:
            if msg.user == 'Human':
                self.memory.chat_memory.add_user_message(msg.content)
            else:
                self.memory.chat_memory.add_ai_message(msg.content)

        # Format the input data
        input_data = {
            'user_input': message,
            'user_interest': user_interest,
            'user_experience': user_experience
        }

        try:
            # Use LangChain to handle the conversation
            output = self.conversation.predict(input=input_data)
        except Exception as e:
            # You might want to log the exception here
            return Response({"error": f"Failed to process your request due to {e}. Please try again later."},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # Save user input and AI's response to the database
        ChatMessage.objects.create(user=user, content=f'Human: {message}')
        ChatMessage.objects.create(user=user, content=f'Assistant: {output}')

        # Send the assistant's message back to the front-end
        return Response({'message': output})

