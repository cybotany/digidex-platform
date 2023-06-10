from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


@method_decorator(csrf_exempt, name='dispatch')
class CEAIdentification(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ip_address = request.data.get('ip_address')
        identifier = request.data.get('identifier')

        if not ip_address or not identifier:
            return Response({'error': 'Missing ip_address or identifier.'}, status=status.HTTP_400_BAD_REQUEST)

        # You can do more things here like associating the IP with a user or a specific device
        return Response({'message': 'CEA successfully registered.'}, status=status.HTTP_200_OK)
