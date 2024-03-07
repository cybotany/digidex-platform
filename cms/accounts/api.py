from rest_framework import viewsets
from accounts import models, serializers

class DigidexUserViewSet(viewsets.ModelViewSet):
    queryset = models.DigidexUser.objects.all()
    serializer_class = serializers.DigidexUserSerializer


class DigidexProfileViewSet(viewsets.ModelViewSet):
    queryset = models.DigidexProfile.objects.all()
    serializer_class = serializers.DigidexProfileSerializer
