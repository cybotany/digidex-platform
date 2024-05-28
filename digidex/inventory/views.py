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
        form = ItemizedDigitForm(request.POST, user=user)
        if form.is_valid():
            category = form.cleaned_data['category']
            _digit = apps.get_model('digitization', 'DigitalObject').objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                user=request.user
            )
            digit = apps.get_model('inventory', 'ItemizedDigit').objects.create(category=category, digit=_digit)
            digit.save()

            digit_page = digit.create_page()
            digit_page.save()
    
            journal = digit.create_journal()
            journal.save()


            if digit_page:
                NearFieldCommunicationTag = apps.get_model('nfc', 'NearFieldCommunicationTag')
                ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
                ntag.digit = digit
                ntag.save()
                return redirect(digit_page.url)
            else:
                return HttpResponseForbidden("Failed to create a detail page for the digitized object.")
    else:
        form = ItemizedDigitForm(user=user)

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
