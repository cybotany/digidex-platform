from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.urls import reverse

from .models import NearFieldCommunicationTag


def route_nfc_link(request, link_uuid):
    nfc_link = get_object_or_404(NearFieldCommunicationTag, uuid=link_uuid)
    try:
        if not nfc_link.tag.active:
            return HttpResponse("This NFC tag is not active.", status=403)
        
        mapped_content = nfc_link.asset
        
        if mapped_content is None:
            return redirect(reverse('nfc:map_nfc', kwargs={'link_uuid': link_uuid}))
        
        return redirect(mapped_content.url)
    
    except ValidationError as e:
        return HttpResponse(str(e), status=400)

@login_required
def map_nfc_link(request, link_uuid):
    user = request.user
    if request.method == 'POST':
        form = NearFieldCommunicationAssetForm(request.POST, user=user)
        if form.is_valid():
            AssetPage = apps.get_model('asset', 'assetpage')
            asset = AssetPage(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                owner=request.user
            )

            inventory = form.cleaned_data.get('inventory')
            if inventory:
                InventoryPage = apps.get_model('inventory', 'inventorypage')
                parent_page = get_object_or_404(InventoryPage, pk=inventory.id)
    
            else:
                TrainerPage = apps.get_model('trainer', 'trainerpage')
                parent_page = get_object_or_404(TrainerPage, owner=user)

            parent_page.add_child(instance=asset)

            if asset:
                nfc_link = get_object_or_404(NearFieldCommunicationTag, uuid=link_uuid)
                nfc_link.asset=asset
                nfc_link.save()          
                return redirect(asset.url)
            else:
                return HttpResponse("Failed to create a detail page for the digitized object.")
    else:
        form = NearFieldCommunicationAssetForm(user=user)

    return render(request, "nfc/includes/add_asset_form.html", {'form': form})
