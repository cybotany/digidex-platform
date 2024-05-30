from django.apps import apps
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from inventory.forms import InventoryCategoryForm, InventoryCategoryDeletionForm


User = get_user_model()

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
    
    return render(request, 'inventory/category/update.html', {'form': form})


@login_required
def delete_category_view(request, category_uuid):
    if request.method == 'POST':
        form = InventoryCategoryDeletionForm(request.POST)
        if form.is_valid():
            category = get_object_or_404(apps.get_model('Inventory', 'Category'), uuid=category_uuid)
            _name = category.name
            category.delete()
            messages.success(request, f'Category {_name} successfully deleted')
            return redirect(reverse('home'))
    else:
        form = InventoryCategoryDeletionForm()
    
    return render(request, 'inventory/category/delete.html', {'form': form})
