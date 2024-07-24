from django.shortcuts import redirect, get_object_or_404

from inventorytags.models import NearFieldCommunicationTag


def link(request, uuid):
    nfc_tag = get_object_or_404(
        NearFieldCommunicationTag,
        uuid=uuid
    )
    tag_url = nfc_tag.get_linked_url()
    return redirect(tag_url)
