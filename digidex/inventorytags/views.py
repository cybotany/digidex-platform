import logging
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.utils.text import slugify
from django.views.decorators.http import require_http_methods

from inventorytags.models import NearFieldCommunicationTag

logger = logging.getLogger(__name__)

@require_http_methods(["GET"])
def link(request, uuid):
    logger.debug("Received request to link view with UUID: %s", uuid)

    # Fetch the NFC tag with related link and owner
    nfc_tag = get_object_or_404(
        NearFieldCommunicationTag.objects.select_related('link', 'owner'),
        uuid=uuid
    )
    logger.debug("Fetched NFC tag: %s", nfc_tag)

    # Define base URL based on the environment
    base_url = 'http://localhost:8000/inv' if settings.DEBUG else 'https://digidex.tech/inv'
    logger.debug("Base URL: %s", base_url)

    # If the NFC Tag has no owner, redirect to the base URL
    if nfc_tag.owner is None:
        logger.debug("NFC tag has no owner, redirecting to base URL.")
        return redirect(base_url)

    # Generate the default URL to redirect to the owner's profile
    linked_url = f'{base_url}/{slugify(nfc_tag.owner.username)}'
    logger.debug("Generated owner-based linked URL: %s", linked_url)

    logger.debug("User sending request: %s", request.user)
    logger.debug("Owner of NFC Tag: %s", nfc_tag.owner)

    # If the request user is the owner, redirect to the NFC tag management page
    if request.user == nfc_tag.owner:
        logger.debug("Request user is the owner, redirecting to NFC tag management page.")
        return redirect(f'{linked_url}/ntag/{nfc_tag.uuid}')

    # Redirect to the owner-entered link URL if it exists
    if nfc_tag.link and nfc_tag.link.url:
        logger.debug("NFC tag has a linked URL, redirecting to: %s", nfc_tag.link.url)
        return redirect(nfc_tag.link.url)
    
    # Redirect to the asset page if it exists
    if nfc_tag.link and nfc_tag.link.asset:
        logger.debug("NFC tag has a linked asset, redirecting to: %s", f'{linked_url}/{nfc_tag.link.asset.slug}')
        return redirect(f'{linked_url}/{nfc_tag.link.asset.slug}')

    # Fallback to redirect to the owner's profile
    logger.debug("No specific URL found, redirecting to the owner's profile page.")
    return redirect(linked_url)
