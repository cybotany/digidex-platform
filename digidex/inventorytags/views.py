from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse

from inventorytags.models import NearFieldCommunicationTag


def link(request, uuid):
    nfc_tag = get_object_or_404(
        NearFieldCommunicationTag.objects.select_related('link'),
        uuid=uuid
    )
    
    if not nfc_tag.active:
        return HttpResponse("This tag is not active.", status=403)

    return redirect(nfc_tag.link.url)
