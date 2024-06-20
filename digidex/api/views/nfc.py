from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from inventory.models import NearFieldCommunicationTag


class RegisterNearFieldCommunicationTag(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        serial_number = request.data.get('serial_number')

        if not serial_number:
            return Response({"error": "Serial Number not provided."}, status=status.HTTP_400_BAD_REQUEST)

        ntag, created = NearFieldCommunicationTag.objects.update_or_create(
            serial_number=serial_number,
            defaults={'active': True}
        )

        absolute_url = request.build_absolute_uri(ntag.url)
        _status = status.HTTP_201_CREATED if created else status.HTTP_200_OK

        return Response({"ntag_url": absolute_url}, status=_status)
