from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from digidex.link.models.nfc import tag

class CreateNtagLink(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        serial_number = request.data.get('serial_number')
        ntag_type = request.data.get('type')
        ntag_use = request.data.get('use')

        if not serial_number:
            return Response({"error": "Serial Number not provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        ntag, created = ntag.NTAG.objects.update_or_create(
            serial_number=serial_number, 
            defaults={'type': ntag_type, 'use': ntag_use}
        )
        ntag_url = request.build_absolute_uri(ntag.get_absolute_url())
        return Response({"ntag_url": ntag_url}, status=status.HTTP_201_CREATED)
