from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from inventory.models import UserInventory
from api.serializers.inventory import UserInventorySerializer


class UserInventoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserInventory.objects.all()
    serializer_class = UserInventorySerializer
    permission_classes = [IsAuthenticated]
