from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory


class ChatbotAPIView(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Define the template for the conversation
        template = """
        You are an experienced head grower at an agritech consulting company.

        {history}
        Human: {human_input}
        Assistant:"""

        self.prompt = PromptTemplate(input_variables=["history", "human_input"], template=template)

        # Initialize LangChain
        self.chatgpt_chain = LLMChain(
            llm=OpenAI(temperature=0, openai_api_key=config('OPENAI_API_KEY')),
            prompt=self.prompt,
            verbose=True,
            memory=ConversationBufferWindowMemory(k=2)
        )

    def post(self, request, *args, **kwargs):
        message = request.data.get('message')

        # Input validation
        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Use LangChain to handle the conversation
            output = self.chatgpt_chain.predict(human_input=message)
        except Exception as e:
            # You might want to log the exception here
            return Response({"error": f"Failed to process your request due to {e}. Please try again later."},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # Send the assistant's message back to the front-end
        return Response({'message': output})
