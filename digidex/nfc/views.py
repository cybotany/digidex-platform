from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.urls import reverse

from .models import NearFieldCommunicationLink
from .forms import NearFieldCommunicationAssetForm


User = get_user_model()


def route_nfc_tag_url(request, nfc_uuid):
    nfc_link = get_object_or_404(NearFieldCommunicationLink, uuid=nfc_uuid)
    try:
        if not nfc_link.tag.active:
            return HttpResponse("This NFC tag is not active.", status=403)
        
        mapped_content = nfc_link.tag.get_mapped_content()
        
        if mapped_content is None:
            return redirect(reverse('nfc:map_nfc_tag', kwargs={'nfc_uuid': nfc_uuid}))
        
        return redirect(mapped_content.url)
    
    except ValidationError as e:
        return HttpResponse(str(e), status=400)

@login_required
def map_nfc_tag(request, nfc_uuid):
    user = request.user
    if request.method == 'POST':
        form = NearFieldCommunicationAssetForm(request.POST, user=user)
        if form.is_valid():
            InventoryPage = apps.get_model('inventory', 'inventorypage')
            AssetPage = apps.get_model('asset', 'assetpage')

            inventory = form.cleaned_data['inventory']
            parent_page = get_object_or_404(InventoryPage, pk=inventory.id)

            asset = AssetPage(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                owner=request.user
            )
            parent_page.add_child(instance=asset)

            if asset:
                nfc_link = get_object_or_404(NearFieldCommunicationLink, uuid=nfc_uuid)
                nfc_link.content_type=ContentType.objects.get_for_model(asset)
                nfc_link.object_id=asset.id
                nfc_link.save()          
                return redirect(asset.url)
            else:
                return HttpResponse("Failed to create a detail page for the digitized object.")
    else:
        form = NearFieldCommunicationAssetForm(user=user)

    return render(request, "nfc/includes/add_asset_form.html", {'form': form})
