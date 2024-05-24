from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from digitization.models import DigitalObject
from api.serializers.digitization import DigitalObjectSerializer


class DigitalObjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DigitalObject.objects.all()
    serializer_class = DigitalObjectSerializer
    permission_classes = [IsAuthenticated]
