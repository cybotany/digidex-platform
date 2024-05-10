from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from nfc.models import NearFieldCommunicationTag


def route_ntag_url(request, _uuid):
    ntag = get_object_or_404(NearFieldCommunicationTag, uuid=_uuid)
    try:
        if not ntag.active:
            return HttpResponse("This NFC tag is not active.", status=403)
        if not ntag.digitized_object:
            if not request.user.is_authenticated:
                login_url = "account_login"
                return redirect(login_url)
            profile_slug = request.user.profile.slug
            return redirect('profiles:link_ntag', profile_slug=profile_slug, ntag_uuid=_uuid)
        return redirect(ntag.digitized_object_page.url)

    except ValidationError as e:
        return HttpResponse(str(e), status=400)
