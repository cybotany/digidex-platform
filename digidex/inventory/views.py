from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from inventory.forms import DigitalObjectForm


User = get_user_model()

@login_required
def add_digit_view(request, ntag_uuid):
    user=request.user
    if request.method == 'POST':
        form = DigitalObjectForm(request.POST, user=user)
        if form.is_valid():
            digit = apps.get_model('inventory', 'DigitalObject').objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                user=request.user
            )
            digit.save()
            digit_page = digit.create_page()
    
            journal = digit.create_journal()
            journal.save()


            if digit_page:
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
