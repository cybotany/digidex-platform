from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from digit.nfc.models import Link


class CreateLink(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        serial_number = kwargs.get('serial_number')
        if not serial_number:
            return Response({"error": "Serial Number not provided."}, status=status.HTTP_400_BAD_REQUEST)
        link, created = Link.objects.get_or_create(serial_number=serial_number)
        link_url = request.build_absolute_uri(link.get_absolute_url())
        return Response({"link_url": link_url}, status=status.HTTP_201_CREATED)
