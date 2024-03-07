from rest_framework import viewsets
from cms.accounts import models, serializers

class DigidexUserViewSet(viewsets.ModelViewSet):
    queryset = models.DigidexUser.objects.all()
    serializer_class = serializers.DigidexUserSerializer
