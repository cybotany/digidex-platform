from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.http import urlencode

from nfc.models import NearFieldCommunicationTag


def route_ntag_url(request, _uuid):
    ntag = get_object_or_404(NearFieldCommunicationTag, uuid=_uuid)
    try:
        if not ntag.active:
            return HttpResponse("This NFC tag is not active.", status=403)
        if not ntag.digitized_object:
            if not request.user.is_authenticated:
                next_url = reverse('profiles:link_ntag', kwargs={'profile_slug': request.user.profile.slug, 'ntag_uuid': _uuid})
                login_url = reverse('account_login')
                login_url_with_next = f"{login_url}?{urlencode({'next': next_url})}"
                return redirect(login_url_with_next)
            return redirect(next_url)
        return redirect(ntag.digitized_object_page.url)

    except ValidationError as e:
        return HttpResponse(str(e), status=400)
