from wagtail.api.v2.router import WagtailAPIRouter

from inventory.api import InventoryPageViewSet

api_router = WagtailAPIRouter('wagtailapi')


api_router.register_endpoint('inventory', InventoryPageViewSet)
