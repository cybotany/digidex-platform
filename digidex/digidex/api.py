from wagtail.api.v2.router import WagtailAPIRouter

from asset.api import AssetPageViewSet
from inventory.api import InventoryPageViewSet
from trainer.api import TrainerPageViewSet


api_router = WagtailAPIRouter('wagtailapi')

api_router.register_endpoint('asset', AssetPageViewSet)
api_router.register_endpoint('inventory', InventoryPageViewSet)
api_router.register_endpoint('trainer', TrainerPageViewSet)
