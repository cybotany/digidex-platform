from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from digidex.link.models import NTAG

class CreateLink(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        ntag_serial_number = kwargs.get('serial_number')
        if not ntag_serial_number:
            return Response({"error": "Serial Number not provided."}, status=status.HTTP_400_BAD_REQUEST)
        ntag, created = NTAG.objects.get_or_create(serial_number=ntag_serial_number)
        ntag_url = request.build_absolute_uri(ntag.get_absolute_url())
        return Response({"ntag_url": ntag_url}, status=status.HTTP_201_CREATED)
