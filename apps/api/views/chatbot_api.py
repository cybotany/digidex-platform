from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
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

        self.prompt = PromptTemplate(input_variables=['history', 'input'], template=self.template)
        self.llm = OpenAI(temperature=0.0, openai_api_key=config('OPENAI_API_KEY'))
        self.memory = ConversationBufferMemory(memory_key='history', ai_prefix="AI Assistant")

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

        print(output)
        return Response({'message': output})
