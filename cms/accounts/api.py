from rest_framework import viewsets
from cms.accounts.models import DigidexUser
from cms.accounts.serializers import DigidexUserSerializer

class DigidexUserViewSet(viewsets.ModelViewSet):
    queryset = DigidexUser.objects.all()
    serializer_class = DigidexUserSerializer
