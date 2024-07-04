from wagtail import hooks
from wagtail.admin.ui.tables import Column
from wagtail.admin.viewsets.pages import PageListingViewSet
from wagtail.admin.panels import FieldPanel, InlinePanel, TabbedInterface, TitleFieldPanel, ObjectList
from wagtail.admin.filters import WagtailFilterSet
from wagtail.admin.viewsets.pages import PageListingViewSet

from inventory.models import Inventory, InventoryProfile, InventoryCategory 


class InventoryProfileFilterSet(PageListingViewSet.filterset_class):
    class Meta:
        model = InventoryProfile
        fields = ["owner"]


class InventoryProfileViewSet(PageListingViewSet):
    icon = "user"
    menu_label = "Inventory"
    add_to_admin_menu = True
    model = InventoryProfile

    # Optional customizations for the listing view
    list_display = ["tag", "content_type", "object_id"]
    list_filter = ["content_type"]

    filterset_class = InventoryProfileFilterSet

    columns = PageListingViewSet.columns + [
        Column("blog_category", label="Category", sort_key="blog_category"),
    ]

    content_panels = [
        TitleFieldPanel('title', classname="title"),
        FieldPanel('date'),
        FieldPanel('body'),
    ]
    sidebar_content_panels = [
        FieldPanel('advert'),
        InlinePanel('related_links', heading="Related links", label="Related link"),
    ]

    edit_handler = TabbedInterface([
        ObjectList([FieldPanel("name")], heading="Details", permission="superuser"),
        ObjectList([FieldPanel("shirt_size")], heading="Preferences"),
    ])

inventory_profile_viewset = InventoryProfileViewSet()
@hooks.register("register_admin_viewset")
def register_inventory_profile_listing_viewset():
    return inventory_profile_viewset
