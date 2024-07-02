from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import NearFieldCommunicationTag, NearFieldCommunicationLink
from .serializers import NearFieldCommunicationTagSerializer, NearFieldCommunicationLinkSerializer


class NearFieldCommunicationTagViewSet(viewsets.ModelViewSet):
    queryset = NearFieldCommunicationTag.objects.all()
    serializer_class = NearFieldCommunicationTagSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        serial_number = request.data.get('serial_number')
        tag_form = request.data.get('tag_form')

        if not serial_number:
            return Response({"error": "Serial Number not provided."}, status=status.HTTP_400_BAD_REQUEST)

        if not tag_form:
            return Response({"error": "Tag Form not provided."}, status=status.HTTP_400_BAD_REQUEST)

        nfc_tag, created = NearFieldCommunicationTag.objects.update_or_create(
            serial_number=serial_number,
            defaults={"tag_form": tag_form}
        )

        serializer = self.get_serializer(nfc_tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


class NearFieldCommunicationLinkViewSet(viewsets.ModelViewSet):
    queryset = NearFieldCommunicationLink.objects.all()
    serializer_class = NearFieldCommunicationLinkSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        uuid = request.data.get('uuid')
        try:
            nfc_tag = NearFieldCommunicationTag.objects.get(uuid=uuid)
        except NearFieldCommunicationTag.DoesNotExist:
            return Response({"error": "NFC Tag not found."}, status=status.HTTP_404_NOT_FOUND)

        nfc_link, created = NearFieldCommunicationLink.objects.get_or_create(tag=nfc_tag)
        nfc_url = nfc_link.get_url()
        absolute_nfc_url = request.build_absolute_uri(nfc_url)
        
        response_data = {
            "nfc_tag_url": absolute_nfc_url
        }
        return Response(response_data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
