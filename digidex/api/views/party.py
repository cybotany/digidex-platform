from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from party.models import UserParty
from api.serializers.party import UserPartySerializer


class PartyDetail(generics.RetrieveAPIView):
    queryset = UserParty.objects.all()
    serializer_class = UserPartySerializer
    permission_classes = [IsAuthenticated]
