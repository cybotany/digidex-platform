from django.apps import apps
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from inventory.forms import DigitalObjectForm, InventoryDigitDeletionForm


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

@login_required
def update_digit_view(request, user_slug, category_slug, digit_slug):
    fullslug = f"{user_slug}/{category_slug}/{digit_slug}"
    digit = get_object_or_404(apps.get_model('inventory', 'DigitalObject'), slug=fullslug)
    if request.method == 'POST':
        form = DigitalObjectForm(request.POST, request.FILES, instance=digit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Digital object successfully updated')
            return redirect(digit.page.url)
    else:
        form = DigitalObjectForm(instance=digit)
    
    return render(request, 'inventory/digit/update.html', {'form': form})


@login_required
def delete_digit_view(request, user_slug, category_slug, digit_slug):
    user = get_object_or_404(User, slug=user_slug)
    if request.method == 'POST':
        form = InventoryDigitDeletionForm(request.POST)
        if form.is_valid():
            fullslug = f"{user_slug}/{category_slug}/{digit_slug}"
            digit = get_object_or_404(apps.get_model('inventory', 'DigitalObject'), slug=fullslug)
            _name = digit.name
            digit.delete()
            messages.success(request, f'Digit {_name} successfully deleted')
            return redirect(user.page.url)
    else:
        form = InventoryDigitDeletionForm()
    
    return render(request, 'inventory/digit/delete.html', {'form': form})
