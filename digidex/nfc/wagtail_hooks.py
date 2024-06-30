from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, InlinePanel

from .forms import NearFieldCommunicationLinkForm
from .models import NearFieldCommunicationTag, NearFieldCommunicationLink


class NearFieldCommunicationTagViewSet(SnippetViewSet):
    model = NearFieldCommunicationTag

    panels = [
        FieldPanel('serial_number'),
        FieldPanel('active'),
        InlinePanel('mapping', label="NTAG Mapping", max_num=1),
    ]

register_snippet(NearFieldCommunicationTagViewSet)


class NearFieldCommunicationLinkViewSet(SnippetViewSet):
    model = NearFieldCommunicationLink
    icon = "link"
    add_to_admin_menu = True
    form = NearFieldCommunicationLinkForm

    list_display = ["tag", "content_type", "object_id"]
    list_filter = ["content_type"]

register_snippet(NearFieldCommunicationLinkViewSet)