from wagtail.api.v2.views import BaseAPIViewSet

from .models import InventoryPage

class InventoryPageViewSet(BaseAPIViewSet):
    """
    http://127.0.0.1:8000/api/v2/inventory/?uuid=1290021b-93e5-481a-97c1-37c9f10c1a2c&fields=uuid,description
    """
    model = InventoryPage

    def get_queryset(self):
        queryset = super().get_queryset()
        uuid = self.request.GET.get('uuid', None)
        if uuid:
            queryset = queryset.filter(uuid=uuid)
        return queryset
