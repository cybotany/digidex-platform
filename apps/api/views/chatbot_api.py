from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai


class ChatbotAPIView(APIView):

    def post(self, request, *args, **kwargs):
        message = request.data.get('message')

        # Input validation
        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Make an API call to OpenAI with the user's message
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a knowledgeable assistant."},
                    {"role": "user", "content": message}
                ]
            )
        except Exception:
            # You might want to log the exception here
            return Response({"error": "Failed to process your request. Please try again later."},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # Extract the assistant's message from the response
        assistant_message = response['choices'][0]['message']['content']

        # Send the assistant's message back to the front-end
        return Response({'message': assistant_message})
