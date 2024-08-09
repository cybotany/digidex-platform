from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods

from inventory.models import NearFieldCommunicationTag, TrainerInventoryPage
from inventory.forms import NearFieldCommunicationTagForm as nfc_tag_form 

@require_http_methods(["GET"])
def link(request, uuid):
    """
    Sends request.user to the asset page if it exists.
    If it doesn't exist they will be redirected
    to the NFC tag management page.
    """

    nfc_tag = get_object_or_404(
        NearFieldCommunicationTag.objects.prefetch_related('records__asset'),
        uuid=uuid
    )

    nfc_record = nfc_tag.records.first()
    if nfc_record and nfc_record.asset:
        return redirect(nfc_record.asset.url)
    return redirect(reverse('manage-tag', args=[str(uuid)]))

@login_required
def manage(request, uuid):
    nfc_tag = get_object_or_404(
        NearFieldCommunicationTag.objects.select_related('owner').prefetch_related('records'),
        uuid=uuid
    )

    base_url = 'http://localhost:8000/' if settings.DEBUG else 'https://digidex.tech/'
    if not nfc_tag.owner:
        messages.error(request, _('Tag not registered.'))
        return redirect(base_url)    

    if request.user != nfc_tag.owner:
        messages.error(request, _('Tag registered by another user.'))
        return redirect(base_url)

    if not nfc_tag.records.exists():
        messages.error(request, _('Tag improperly configured.'))
        return redirect(base_url)

    user_inventory = get_object_or_404(TrainerInventoryPage, owner=request.user)

    if request.method == "POST":
        nfc_record = nfc_tag.records.first()
        form = nfc_tag_form(request.POST, instance=nfc_record, user_inventory=user_inventory)
        if form.is_valid():
            form.save()
            messages.success(request, _('Tag successfully linked.'))
            return redirect(user_inventory.url)
    else:
        nfc_record = nfc_tag.records.first()
        form = nfc_tag_form(instance=nfc_record, user_inventory=user_inventory)

    return render(request, 'inventory/includes/manage_nfc_tag.html', {'form': form})
