from django.conf import settings
from django.shortcuts import redirect, get_object_or_404

from inventorytags.models import NearFieldCommunicationTag


def link(request, uuid):
    nfc_tag = get_object_or_404(
        NearFieldCommunicationTag.objects.select_related('link', 'owner'),
        uuid=uuid
    )

    if not nfc_tag.owner:
        pass
    tag_url = nfc_tag.link.get_url(user=request.user)
    return redirect(tag_url)
