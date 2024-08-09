from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from inventory.models import NearFieldCommunicationTag, NearFieldCommunicationLink

class NearFieldCommunicationTagViewSet(SnippetViewSet):
    model = NearFieldCommunicationTag
    icon = "tag"
    menu_label = "NFC Tags"
    menu_name = "nfc-tags"
    list_filter = {
        "label": ["icontains"],
        "type": ["exact"],
    }

    panels = [
        MultiFieldPanel([
            FieldPanel("owner"),
            FieldPanel("label"),
            FieldPanel("type"),
        ], heading="NFC Tag Information"),
    ]

    def get_queryset(self, request):
        """
        Filter the queryset to only show instances where the owner is the current user.
        """
        qs = super().get_queryset(request)
        if qs is None:
            qs = self.model.objects.all()
        return qs.filter(owner=request.user)


class NearFieldCommunicationLinkViewSet(SnippetViewSet):
    model = NearFieldCommunicationLink
    icon = "link"
    menu_label = "NFC Tag Links"
    menu_name = "nfc-links"

    panels = [
        FieldPanel("asset"),
    ]


class NearFieldCommunicationViewSetGroup(SnippetViewSetGroup):
    items = (NearFieldCommunicationTagViewSet, NearFieldCommunicationLinkViewSet)
    menu_icon = "table"
    menu_label = "NFC"
    menu_name = "nfc"


register_snippet(NearFieldCommunicationViewSetGroup)
