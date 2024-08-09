from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods

from inventory.models import NearFieldCommunicationTag


@require_http_methods(["GET"])
def link(request, uuid):
    """
    Sends request.user to the asset page if it exists.
    If it doesn't exist they will be redirected
    to the NFC tag management page.
    """

    nfc_tag = get_object_or_404(
        NearFieldCommunicationTag.objects
        .select_related('owner')
        .prefetch_related('records__asset'),
        uuid=uuid
    )

    nfc_record = nfc_tag.records.first()
    if nfc_record and nfc_record.asset:
        return redirect(nfc_record.asset.url)

    base_url = 'http://localhost:8000/' if settings.DEBUG else 'https://digidex.tech/'
    if not nfc_tag.owner:
        messages.error(request, _('Tag not registered.'))
        return redirect(base_url)    

    if request.user != nfc_tag.owner:
        messages.error(request, _('Tag registered by another user.'))
        return redirect(base_url)

    url = reverse('wagtailsnippets_inventory_ntags:edit', args=[nfc_tag.id])
    return redirect(url)
