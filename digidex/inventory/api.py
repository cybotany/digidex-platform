from wagtail.models import Page
from wagtail.api.v2.views import PagesAPIViewSet

from .models import InventoryPage


class InventoryPageViewSet(PagesAPIViewSet):
    model = InventoryPage

    def get_queryset(self):
        queryset = super().get_queryset()
        uuid = self.request.GET.get('uuid', None)
        if uuid:
            try:
                inventory_page = InventoryPage.objects.get(uuid=uuid)
                queryset = inventory_page.get_descendants().live().public()
            except InventoryPage.DoesNotExist:
                queryset = Page.objects.none()
        return queryset
