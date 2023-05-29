from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.contrib.auth.models import User
from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
import openai


class CybotView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        openai.api_key = config('OPENAI_API_KEY')
        message = request.data.get('message')

        # Make an API call to OpenAI with the user's message
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant."},
                {"role": "user", "content": message}
            ]
        )

        # Extract the assistant's message from the response
        assistant_message = response['choices'][0]['message']['content']

        # Send the assistant's message back to the front-end
        return Response({'message': assistant_message})


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
