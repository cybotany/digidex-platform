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
    if request.method == 'POST':
        form = DigitalObjectForm(request.POST)
        name = form.cleaned_data['name']
        if form.is_valid():
            digital_object = apps.get_model('inventory', 'DigitalObjectPage').objects.create(
                title=f"{name.title()}'s Inventory",
                slug=slugify(name),
                owner=page_owner,
                name=name,
                description=form.cleaned_data['description']
            )
            digit.save()


            if digit:
                NearFieldCommunicationTag = apps.get_model('nfc', 'NearFieldCommunicationTag')
                ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
                ntag.digital_object = digit
                ntag.save()
                return redirect(digit_page.url)
            else:
                return HttpResponseForbidden("Failed to create a detail page for the digitized object.")
    else:
        form = DigitalObjectForm(user=user)

    return render(request, "inventory/digit/add.html", {'form': form})
