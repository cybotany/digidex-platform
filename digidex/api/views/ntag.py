from rest_framework import viewsets

from nfc.models import NearFieldCommunicationTag
from nfc.serializers import NearFieldCommunicationTagSerializer


class NearFieldCommunicationTagViewSet(viewsets.ModelViewSet):
    queryset = NearFieldCommunicationTag.objects.all()
    serializer_class = NearFieldCommunicationTagSerializer

    def perform_create(self, serializer):
        serializer.save()
