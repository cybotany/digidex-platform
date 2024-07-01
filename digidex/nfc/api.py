from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from nfc.models import NearFieldCommunicationTag, NearFieldCommunicationLink


class RegisterNearFieldCommunicationTag(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        serial_number = request.data.get('serial_number')

        if not serial_number:
            return Response({"error": "Serial Number not provided."}, status=status.HTTP_400_BAD_REQUEST)

        nfc_tag, _ = NearFieldCommunicationTag.objects.update_or_create(
            serial_number=serial_number,
            defaults={'active': True}
        )
        nfc_link, created = NearFieldCommunicationLink.objects.get_or_create(
            tag=nfc_tag
        )

        nfc_url = nfc_link.get_url()

        absolute_nfc_url = request.build_absolute_uri(nfc_url)
        request_status = status.HTTP_201_CREATED if created else status.HTTP_200_OK

        return Response({"nfc_tag_url": absolute_nfc_url}, status=request_status)
