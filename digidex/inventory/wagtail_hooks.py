from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet

from inventory.models import InventoryIndex


class InventoryIndexListingViewSet(PageListingViewSet):
    icon = "desktop"
    menu_label = "User Inventory"
    add_to_admin_menu = True
    model = InventoryIndex


inventory_index_listing_viewset = InventoryIndexListingViewSet("user_inventory")
@hooks.register("register_admin_viewset")
def register_inventory_index_listing_viewset():
    return inventory_index_listing_viewset
