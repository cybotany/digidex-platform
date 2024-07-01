from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .forms import NearFieldCommunicationLinkForm
from .models import NearFieldCommunicationLink


class NearFieldCommunicationLinkViewSet(SnippetViewSet):
    model = NearFieldCommunicationLink
    icon = "link"
    add_to_admin_menu = True
    form = NearFieldCommunicationLinkForm

    list_display = ["tag", "content_type", "object_id"]
    list_filter = ["content_type"]

register_snippet(NearFieldCommunicationLinkViewSet)
