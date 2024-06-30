from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, InlinePanel

from .models import NearFieldCommunicationTag


class NearFieldCommunicationTagViewSet(SnippetViewSet):
    model = NearFieldCommunicationTag

    panels = [
        FieldPanel('serial_number'),
        FieldPanel('active'),
        InlinePanel('mapping', label="NTAG Mapping", max_num=1),
    ]

register_snippet(NearFieldCommunicationTagViewSet)
