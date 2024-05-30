from django.apps import apps
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from inventory.forms import ItemizedDigitForm, InventoryDeletionForm, InventoryCategoryForm


User = get_user_model()

@login_required
def link_ntag_view(request, ntag_uuid):
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
        form = ItemizedDigitForm(user=user)

    return render(request, "inventory/link_ntag.html", {'form': form})


@login_required
def update_category_view(request, category_uuid):
    category = get_object_or_404(apps.get_model('Inventory', 'Category'), uuid=category_uuid)
    if request.method == 'POST':
        form = InventoryCategoryForm(request.POST, instance=category)
        if form.is_valid():
            updated_category = form.save()
            messages.success(request, f'{updated_category.name} successfully updated')
            return redirect(updated_category._page.url)
    else:
        form = InventoryCategoryForm(instance=category)
    
    return render(request, 'inventory/update_category.html', {'form': form})


@login_required
def delete_category_view(request, category_uuid):
    if request.method == 'POST':
        form = InventoryDeletionForm(request.POST)
        if form.is_valid():
            category = get_object_or_404(apps.get_model('Inventory', 'Category'), uuid=category_uuid)
            _name = category.name
            category.delete()
            messages.success(request, f'Category {_name} successfully deleted')
            return redirect(reverse('home'))
    else:
        form = InventoryDeletionForm()
    
    return render(request, 'inventory/delete_category.html', {'form': form})


@login_required
def update_digit_view(request, digit_uuid):
    digit = get_object_or_404(apps.get_model('Inventory', 'ItemizedDigit'), uuid=digit_uuid)
    if request.method == 'POST':
        form = ItemizedDigitForm(request.POST, request.FILES, instance=digit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')
            return redirect(digit.page.url)
    else:
        form = ItemizedDigitForm(instance=digit)
    
    return render(request, 'inventory/update_digit.html', {'form': form})


@login_required
def delete_digit_view(request, digit_uuid):
    if request.method == 'POST':
        form = InventoryDeletionForm(request.POST)
        if form.is_valid():
            digit = get_object_or_404(apps.get_model('Inventory', 'ItemizedDigit'), uuid=digit_uuid)
            _name = digit.name
            digit.delete()
            messages.success(request, f'Digit {_name} successfully deleted')
            return redirect(reverse('home'))
    else:
        form = InventoryDeletionForm()
    
    return render(request, 'inventory/delete_digit.html', {'form': form})
