from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.routers import DefaultRouter

from nearfieldcommunication.models import NearFieldCommunicationTag
from nearfieldcommunication.serializers import NearFieldCommunicationTagSerializer


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

router = DefaultRouter()
router.register(r'nfc', NearFieldCommunicationTagViewSet)
