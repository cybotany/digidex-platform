from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain.prompts.prompt import PromptTemplate

from apps.accounts.models import Profile
from apps.chatbot.models import ChatMessage


class ChatbotAPIView(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.template = """
        This is a friendly conversatiion between a human and an AI.
        The AI is talkative and provides lots of specific details from its context.
        If the AI does not know the answer to a question, it truthfully says it does not know.

        Current Conversation:
        {history}
        Human: {input}
        AI Assistant:
        """

        # Define the prompt
        self.prompt = PromptTemplate(input_variables=['history', 'input'], template=self.template)
        self.llm = ChatOpenAI(temperature=0.0, openai_api_key=config('OPENAI_API_KEY'))
        self.memory = ConversationSummaryBufferMemory(llm=self.llm, max_tokens=0)

        # Initialize LangChain
        self.conversation = ConversationChain(
            llm=self.llm,
            prompt=self.prompt,
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

        try:
            # Use LangChain to handle the conversation
            output = self.conversation.predict(input=message)
        except Exception as e:
            # You might want to log the exception here
            return Response({"error": f"Failed to process your request due to {e}. Please try again later."},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # Save user input and AI's response to the database
        ChatMessage.objects.create(user=user, content=f'Human: {message}')
        ChatMessage.objects.create(user=user, content=f'AI: {output}')

        # Send the assistant's message back to the front-end
        return Response({'message': output})
