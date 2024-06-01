from django.apps import apps
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from inventory.forms import DigitalObjectForm, InventoryDigitDeletionForm


User = get_user_model()

@login_required
def add_digit_view(request, user_slug, ntag_uuid):
    user = request.user
    if request.method == 'POST':
        form = DigitalObjectForm(request.POST, user=user)
        if form.is_valid():
            category = form.cleaned_data['category']
            _digit = apps.get_model('digitization', 'DigitalObject').objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                user=request.user
            )
            _digit.save()
            digit = apps.get_model('inventory', 'ItemizedDigit').objects.create(category=category, digit=_digit)
            digit.save()
            digit_page = digit.create_page()
    
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
        form = DigitalObjectForm(user=user)

    return render(request, "inventory/digit/add.html", {'form': form})

@login_required
def update_digit_view(request, user_slug, category_slug, digit_slug):
    digit = get_object_or_404(apps.get_model('inventory', 'ItemizedDigit'), uuid=digit_uuid)
    if request.method == 'POST':
        form = DigitalObjectForm(request.POST, request.FILES, instance=digit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')
            return redirect(digit.page.url)
    else:
        form = DigitalObjectForm(instance=digit)
    
    return render(request, 'inventory/digit/update.html', {'form': form})


@login_required
def delete_digit_view(request, user_slug, category_slug, digit_slug):
    if request.method == 'POST':
        form = InventoryDigitDeletionForm(request.POST)
        if form.is_valid():
            digit = get_object_or_404(apps.get_model('inventory', 'ItemizedDigit'), uuid=digit_uuid)
            _name = digit.name
            digit.delete()
            messages.success(request, f'Digit {_name} successfully deleted')
            return redirect(reverse('home'))
    else:
        form = InventoryDigitDeletionForm()
    
    return render(request, 'inventory/digit/delete.html', {'form': form})
