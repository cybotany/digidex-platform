from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.urls import reverse

from nearfieldcommunication.models import NearFieldCommunicationTag


def route_nfc_link(request, nfc_uuid):
    nfc_link = get_object_or_404(NearFieldCommunicationTag, uuid=nfc_uuid)
    try:
        if not nfc_link.tag.active:
            return HttpResponse("This NFC tag is not active.", status=403)
        
        mapped_content = nfc_link.asset
        
        if mapped_content is None:
            return redirect(reverse('nfc:map_nfc', kwargs={'nfc_uuid': nfc_uuid}))
        
        return redirect(mapped_content.url)
    
    except ValidationError as e:
        return HttpResponse(str(e), status=400)
