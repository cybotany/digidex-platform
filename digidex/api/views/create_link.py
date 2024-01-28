from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from digidex.link.models import NFC

class CreateLink(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        ntag_serial_number = kwargs.get('serial_number')
        if not ntag_serial_number:
            return Response({"error": "Serial Number not provided."}, status=status.HTTP_400_BAD_REQUEST)
        nfc, created = NFC.objects.get_or_create(serial_number=ntag_serial_number)
        nfc_url = request.build_absolute_uri(nfc.get_absolute_url())
        return Response({"nfc_url": nfc_url}, status=status.HTTP_201_CREATED)
