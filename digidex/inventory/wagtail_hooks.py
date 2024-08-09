from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from inventory.models import NearFieldCommunicationTag

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


register_snippet(NearFieldCommunicationTagViewSet)
