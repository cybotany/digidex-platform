from rest_framework import generics

from inventory.models import UserInventory
from api.serializers.inventory import UserInventorySerializer


class UserInventoryListView(generics.ListAPIView):
    serializer_class = UserInventorySerializer

    def get_queryset(self):
        profile_page_id = self.kwargs['profile_page_id']
        return UserInventory.objects.filter(profile_page_id=profile_page_id)
