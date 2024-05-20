from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from digitization.models import UserDigit
from api.serializers.digitization import UserDigitSerializer


class UserDigitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserDigit.objects.all()
    serializer_class = UserDigitSerializer
    permission_classes = [IsAuthenticated]
