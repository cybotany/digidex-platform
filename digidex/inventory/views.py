from django.apps import apps
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from inventory.forms import ItemizedDigitForm

User = get_user_model()


@login_required
def link_ntag(request, ntag_uuid):
    user = request.user
    if request.method == 'POST':
        form = ItemizedDigitForm(request.POST)
        if form.is_valid():
            digit = form.save()
            
            journal = digit.create_journal()
            journal.save()

            digit_page = digit.create_digit_page(user.page)
            
            if digit_page:
                NearFieldCommunicationTag = apps.get_model('nfc', 'NearFieldCommunicationTag')
                ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
                ntag.digit = digit
                ntag.save()
                return redirect(digit_page.url)
            else:
                return HttpResponseForbidden("Failed to create a detail page for the digitized object.")
    else:
        form = ItemizedDigitForm()

    return render(request, "inventory/link_ntag.html", {'form': form})


@login_required
def delete_digit(request, digit_uuid):
    if request.method == 'POST':
        user = request.user
        digit = get_object_or_404(apps.get_model('inventory', 'ItemizedDigitForm'), uuid=digit_uuid)
        digit.delete()
        messages.success(request, 'Digital object deleted successfully.')
        return redirect(user.page.url)
    return redirect(user.page.url)
