from wagtail import hooks
from wagtail.admin.ui.tables import Column
from wagtail.admin.viewsets.pages import PageListingViewSet
from wagtail.admin.panels import FieldPanel, InlinePanel, TabbedInterface, TitleFieldPanel, ObjectList
from wagtail.admin.viewsets.pages import PageListingViewSet

from inventory.models import Inventory 


class InventoryFilterSet(PageListingViewSet.filterset_class):
    class Meta:
        model = Inventory
        fields = ["owner"]


class InventoryViewSet(PageListingViewSet):
    icon = "desktop"
    menu_label = "Inventory"
    add_to_admin_menu = True
    model = Inventory

    filterset_class = InventoryFilterSet

    # columns = PageListingViewSet.columns + [
    #     Column("name", label="Category", sort_key="blog_category"),
    # ]


inventory_viewset = InventoryViewSet("inventory_listing")
@hooks.register("register_admin_viewset")
def register_inventory_listing_viewset():
    return inventory_viewset
