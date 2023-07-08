from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain.prompts.prompt import PromptTemplate


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

        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            output = self.conversation.predict(input=message)
        except Exception as e:
            print(e)
            return Response({"error": f"Failed to process your request due to {e}. Please try again later."},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response({'message': output})
