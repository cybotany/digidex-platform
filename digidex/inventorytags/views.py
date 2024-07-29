from django.shortcuts import redirect, get_object_or_404

from inventorytags.models import NearFieldCommunicationTag


def link(request, uuid):
    nfc_tag = get_object_or_404(
        NearFieldCommunicationTag.objects.select_related('link'),
        uuid=uuid
    )
    tag_url = nfc_tag.link.url
    return redirect(tag_url)
