from django.apps import apps
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from digitization.forms import DigitalObjectForm

User = get_user_model()


@login_required
def link_ntag(request, ntag_uuid):
    user = request.user
    if request.method == 'POST':
        form = DigitalObjectForm(request.POST)
        if form.is_valid():
            digital_object = form.save()
            user.party.add_digit(digital_object)
            
            journal = digital_object.create_journal()
            journal.save()

            digit_parent_page = user.profile.page
            digital_object_page = digital_object.create_digit_page(digit_parent_page)
            
            if digital_object_page:
                NearFieldCommunicationTag = apps.get_model('nfc', 'NearFieldCommunicationTag')
                ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
                ntag.digit = digital_object
                ntag.save()
                return redirect(digital_object_page.url)
            else:
                return HttpResponseForbidden("Failed to create a detail page for the digitized object.")
    else:
        form = DigitalObjectForm()

    return render(request, "digitization/link_ntag.html", {'form': form})


@login_required
def delete_digit(request, digit_uuid):
    if request.method == 'POST':
        user = request.user
        digit = get_object_or_404(apps.get_model('digitization', 'DigitalObject'), uuid=digit_uuid)
        digit.delete()
        messages.success(request, 'Digital object deleted successfully.')
        return redirect(user.profile.page.url)
    return redirect(user.profile.page.url)
