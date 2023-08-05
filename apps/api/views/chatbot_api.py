from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.chatbot.chat_service import ChatService


class ChatbotAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Get the message and check it's not empty
        message = request.data.get('message')
        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        chat_service = ChatService()

        try:
            output = chat_service.converse(message)
            chat_service.save_message('User', message)
            chat_service.save_message('AI', output)

        except Exception as e:
            return Response({"error": f"Failed to process your request due to {e}. Please try again later."},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response({'message': output})
