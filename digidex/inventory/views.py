from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.utils.text import slugify
from django.views.decorators.http import require_http_methods

from inventory.models import NearFieldCommunicationTag


@require_http_methods(["GET"])
def link(request, uuid):

    # Fetch the NFC tag with related link and owner
    nfc_tag = get_object_or_404(
        NearFieldCommunicationTag.objects.select_related('link', 'owner'),
        uuid=uuid
    )

    # Define base URL based on the environment
    base_url = 'http://localhost:8000/inv' if settings.DEBUG else 'https://digidex.tech/inv'

    # If the NFC Tag has no owner, redirect to the base URL
    if nfc_tag.owner is None:
        return redirect(base_url)

    # Generate the default URL to redirect to the owner's profile
    linked_url = f'{base_url}/{slugify(nfc_tag.owner.username)}'

    # Redirect to the asset page if it exists
    if nfc_tag.link and nfc_tag.link.asset:
        return redirect(f'{linked_url}/{nfc_tag.link.asset.slug}')

    # If the request user is the owner, redirect to the NFC tag management page
    if request.user == nfc_tag.owner:
        return redirect(f'{linked_url}/ntag/{nfc_tag.uuid}')

    # Fallback to redirect to the owner's profile
    return redirect(linked_url)
