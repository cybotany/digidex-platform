from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.urls import reverse

from nfc.models import NearFieldCommunicationTag


def route_ntag_url(request, ntag_uuid):
    ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
    try:
        if not ntag.active:
            return HttpResponse("This NFC tag is not active.", status=403)
        if not ntag.digital_object:
            url = reverse('inventory:add_digit', kwargs={'ntag_uuid': ntag_uuid})
            return redirect(url)
        return redirect(ntag.digital_object.page.url)

    except ValidationError as e:
        return HttpResponse(str(e), status=400)
