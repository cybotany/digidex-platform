from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from party.models import UserParty
from api.serializers.party import UserPartySerializer


class UserPartyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserParty.objects.all()
    serializer_class = UserPartySerializer
    permission_classes = [IsAuthenticated]
