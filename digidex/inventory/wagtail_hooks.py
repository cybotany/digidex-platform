from wagtail.admin.panels import FieldPanel, InlinePanel, TabbedInterface, TitleFieldPanel, ObjectList
from wagtail.admin.filters import WagtailFilterSet
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from inventory.models import Inventory


class InventoryFilterSet(WagtailFilterSet):
    class Meta:
        model = Inventory
        fields = ["content_type"]


class InventoryViewSet(SnippetViewSet):
    model = Inventory
    add_to_admin_menu = True

    # Optional customizations for the listing view
    list_display = ["tag", "content_type", "object_id"]
    list_filter = ["content_type"]

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

register_snippet(Inventory)
