from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import NearFieldCommunicationTag


class NearFieldCommunicationTagViewSet(SnippetViewSet):
    model = NearFieldCommunicationTag
    icon = "tag"
    add_to_admin_menu = True

    list_display = ["tag_form", "active"]
    list_filter = ["tag_form", "active"]

register_snippet(NearFieldCommunicationTagViewSet)
