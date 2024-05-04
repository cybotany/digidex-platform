from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from nfc.models import NearFieldCommunicationTag

def route_ntag_url(request, _uuid):
    try:
        ntag = NearFieldCommunicationTag.objects.get(uuid=_uuid)
        if not ntag.digitized_object:
            return redirect('digitization:link_ntag', ntag_uuid=_uuid)
        url = ntag.get_digitized_asset_url()
        return redirect(url)
    except ValidationError as e:
        return HttpResponse(str(e), status=400)
