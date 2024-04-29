from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DigitAPI(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            # Perform logic to create or link digit
            return Response({'redirect_url': 'path_to_digit_registration_form'}, status=status.HTTP_302_FOUND)
        return Response(status=status.HTTP_403_FORBIDDEN)
