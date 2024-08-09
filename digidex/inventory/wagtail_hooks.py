from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

from inventory.models import NearFieldCommunicationTag

class NearFieldCommunicationTagViewSet(SnippetViewSet):
    model = NearFieldCommunicationTag
    icon = "tag"
    menu_label = "NFC Tags"
    menu_name = "ntags"
    menu_order = 300
    name = "ntags"
    add_to_admin_menu = True
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
        InlinePanel("records", label="NFC Tag Records", min_num=0, max_num=1),
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
