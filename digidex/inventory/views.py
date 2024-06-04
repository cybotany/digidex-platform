from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from inventory.forms import DigitalObjectForm

User = get_user_model()

@login_required
def add_digit_view(request, ntag_uuid, user_slug):
    user_profile = get_object_or_404(apps.get_model('inventory', 'UserProfilePage'), slug=user_slug)
    party_category_page = user_profile.get_children().type(apps.get_model('inventory', 'InventoryCategoryPage')).filter(slug='party').first()
    user = user_profile.owner

    if request.method == 'POST':
        form = DigitalObjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            digital_object_page = apps.get_model('inventory', 'DigitalObjectPage')(
                title=f"{name.title()}'s Inventory",
                slug=slugify(name),
                owner=user,
                name=name,
                description=form.cleaned_data['description'],
            )
            if party_category_page:
                party_category_page.add_child(instance=digital_object_page)
                digital_object_page.save_revision().publish()

                if digital_object_page:
                    NearFieldCommunicationTag = apps.get_model('nfc', 'NearFieldCommunicationTag')
                    ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
                    ntag.page = digital_object_page
                    ntag.save()
                    return redirect(digital_object_page.url)
                else:
                    return HttpResponseForbidden("Failed to create a detail page for the digitized object.")
            else:
                return HttpResponseForbidden("Party category page not found.")
    else:
        form = DigitalObjectForm()

    return render(request, "inventory/digit/add.html", {'form': form})
