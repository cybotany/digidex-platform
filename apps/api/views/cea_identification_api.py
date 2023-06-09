from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CEARegister(APIView):
    def post(self, request):
        ip_address = request.data.get('ip_address')
        identifier = request.data.get('identifier')
        # You can do more things here like associating the IP with a user or a specific device
        return Response({'message': 'CEA successfully registered.'}, status=status.HTTP_200_OK)
