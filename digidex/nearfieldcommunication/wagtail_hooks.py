from wagtail.admin.filters import WagtailFilterSet
from wagtail.snippets.models import register_snippet
from wagtail.admin.ui.tables import UpdatedAtColumn
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import TabbedInterface, TitleFieldPanel, ObjectList, FieldPanel

from nearfieldcommunication.models import NearFieldCommunicationTag


class NearFieldCommunicationTagFilterSet(WagtailFilterSet):
    class Meta:
        model = NearFieldCommunicationTag
        fields = ["tag_form", "active", "created_at", "last_modified"]


class NearFieldCommunicationTagViewSet(SnippetViewSet):
    model = NearFieldCommunicationTag
    icon = "tag"
    menu_label = "NFC Tags"
    menu_name = "ntags"
    list_display = ["tag_form", "active", "created_at", "last_modified"]
    list_per_page = 50
    copy_view_enabled = False
    inspect_view_enabled = True
    admin_url_namespace = "nfc_views"
    add_to_admin_menu = True
    base_url_path = "internal/nfc/"
    filterset_class = NearFieldCommunicationTagFilterSet

    edit_handler = TabbedInterface(
        [
            ObjectList(
                [FieldPanel("tag_form")],
                heading="Tag Form"
            ),
            ObjectList(
                [FieldPanel("active")],
                heading="Status"
            ),
        ]
    )

register_snippet(NearFieldCommunicationTagViewSet)
