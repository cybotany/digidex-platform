from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import TabbedInterface, TitleFieldPanel, ObjectList, FieldPanel


from inventory.models import InventoryIndex, InventoryLink


class InventoryIndexListingViewSet(PageListingViewSet):
    icon = "desktop"
    menu_label = "User Inventory"
    add_to_admin_menu = True
    model = InventoryIndex


inventory_index_listing_viewset = InventoryIndexListingViewSet("user_inventory")
@hooks.register("register_admin_viewset")
def register_inventory_index_listing_viewset():
    return inventory_index_listing_viewset


class InventoryLinkViewSet(SnippetViewSet):
    model = InventoryLink
    icon = "link"
    menu_label = "NFC Links"
    menu_name = "links"
    list_display = ["tag", "resource", ]
    list_per_page = 50
    copy_view_enabled = False
    inspect_view_enabled = True
    admin_url_namespace = "inventory_views"
    add_to_admin_menu = True
    base_url_path = "internal/inventory/link"

    panels = [
        TitleFieldPanel("resource"),
    ]


register_snippet(InventoryLinkViewSet)
