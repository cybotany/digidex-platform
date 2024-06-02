from django.apps import apps
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from inventory.forms import JournalEntryForm, InventoryDigitDeletionForm


User = get_user_model()

@login_required
def update_journal_entry_view(request, user_slug, category_slug, digit_slug):
    fullslug = f"{user_slug}/{category_slug}/{digit_slug}"
    digit = get_object_or_404(apps.get_model('inventory', 'DigitalObject'), slug=fullslug)
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, request.FILES, instance=digit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Digital object successfully updated')
            return redirect(digit.page.url)
    else:
        form = JournalEntryForm(instance=digit)
    
    return render(request, 'inventory/digit/update.html', {'form': form})


@login_required
def delete_journal_entry_view(request, user_slug, category_slug, digit_slug):
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
