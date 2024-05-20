from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from profiles.models import UserProfile
from api.serializers.profiles import UserProfileSerializer


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
