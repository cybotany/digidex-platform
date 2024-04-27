from rest_framework import viewsets

from nfc import serializers, models

class NearFieldCommunicationTagViewSet(viewsets.ModelViewSet):

    queryset = models.NearFieldCommunicationTag.objects.all()
    serializer_class = serializers.NearFieldCommunicationTagSerializer

    def perform_create(self, serializer):
        # Here you can add any custom logic you need before saving a new NFC Tag
        serializer.save()
