from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.urls import reverse

from nearfieldcommunication.models import NearFieldCommunicationTag


def route_nfc_link(request, nfc_uuid):
    ntag = get_object_or_404(NearFieldCommunicationTag, uuid=nfc_uuid)
    try:
        if not ntag.active:
            return HttpResponse("This NFC tag is not active.", status=403)
        
        return redirect(ntag.get_url())
    
    except ValidationError as e:
        return HttpResponse(str(e), status=400)