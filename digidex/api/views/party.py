from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from party.models import UserParty
from api.serializers.party import UserPartySerializer


class UserPartyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserPartySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return UserParty.objects.filter(user=self.request.user)
