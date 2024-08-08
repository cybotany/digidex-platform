from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

from inventory.models import NearFieldCommunicationTag

class NearFieldCommunicationTagViewSet(SnippetViewSet):
    model = NearFieldCommunicationTag

    panels = [
        MultiFieldPanel([
            FieldPanel("label"),
            FieldPanel("type"),
            FieldPanel("form"),
        ], heading="NFC Tag Information"),
        InlinePanel("records", label="NFC Tag Records"),
    ]


register_snippet(NearFieldCommunicationTagViewSet)
