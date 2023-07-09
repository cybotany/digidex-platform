from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.utils.chat_service import ChatService


class ChatbotAPIView(APIView):
    def post(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation_id')
        message = request.data.get('message')

        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        chat_service = ChatService()

        try:
            output = chat_service.converse(message)
            chat_service.save_message(conversation_id, message, True)
            chat_service.save_message(conversation_id, output, False)

        except Exception as e:
            print(e)
            return Response({"error": f"Failed to process your request due to {e}. Please try again later."},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response({'message': output})
