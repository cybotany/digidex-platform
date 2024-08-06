from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet

from inventory.models import InventoryAssetPage


class UserAssetListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = "User Assets"
    add_to_admin_menu = True
    model = InventoryAssetPage

user_asset_listing_viewset = UserAssetListingViewSet("user_assets")

@hooks.register("register_admin_viewset")
def register_user_asset_listing_viewset():
    return user_asset_listing_viewset
