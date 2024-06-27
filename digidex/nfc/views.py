from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.urls import reverse

from .models import NearFieldCommunicationTag, NearFieldCommunicationLink
from .forms import NearFieldCommunicationAssetForm


User = get_user_model()


def route_nfc_tag_url(request, ntag_uuid):
    ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
    try:
        if not ntag.active:
            return HttpResponse("This NFC tag is not active.", status=403)
        
        mapped_content = ntag.get_mapped_content()
        
        if mapped_content is None:
            return redirect(reverse('map_nfc_tag', kwargs={'ntag_uuid': ntag_uuid}))
        
        return redirect(mapped_content.url)
    
    except ValidationError as e:
        return HttpResponse(str(e), status=400)

@login_required
def map_nfc_tag(request, ntag_uuid):
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
                ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
                
                NearFieldCommunicationLink.objects.create(
                    tag=ntag,
                    content_type=ContentType.objects.get_for_model(asset),
                    object_id=asset.id
                )
                
                return redirect(asset.url)
            else:
                return HttpResponse("Failed to create a detail page for the digitized object.")
    else:
        form = NearFieldCommunicationAssetForm(user=user)

    return render(request, "nfc/includes/add_asset_form.html", {'form': form})
