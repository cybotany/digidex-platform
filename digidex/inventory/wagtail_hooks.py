from wagtail.admin.ui.tables import UpdatedAtColumn
from wagtail.admin.filters import WagtailFilterSet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import TabbedInterface, TitleFieldPanel, ObjectList, FieldPanel

from inventory.models import InventoryLink
from nearfieldcommunication.models import NearFieldCommunicationTag


class InventoryLinkViewSet(SnippetViewSet):
    model = InventoryLink
    icon = "link"
    menu_label = "NFC Links"
    menu_name = "links"


class NearFieldCommunicationTagViewSet(SnippetViewSet):
    model = NearFieldCommunicationTag
    icon = "tag"
    menu_label = "NFC Tags"
    menu_name = "ntags"


class InventoryTagLinkViewSetGroup(SnippetViewSetGroup):
    items = (InventoryLinkViewSet, NearFieldCommunicationTagViewSet)
    menu_label = "Inventory"
    menu_icon = "tablet-alt"
    menu_name = "inventory"


register_snippet(InventoryTagLinkViewSetGroup)
