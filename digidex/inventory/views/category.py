from django.apps import apps
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from inventory.forms import InventoryCategoryForm, InventoryCategoryDeletionForm


User = get_user_model()

def update_category_view(request, user_slug, category_slug):
    fullslug = f"{user_slug}/{category_slug}"
    category = get_object_or_404(apps.get_model('inventory', 'Category'), slug=fullslug)
    
    if request.method == 'POST':
        form = InventoryCategoryForm(request.POST)
        if form.is_valid():
            category.name = form.cleaned_data['name']
            category.description = form.cleaned_data['description']
            category.save()
            messages.success(request, f'{category.name} successfully updated')
            return redirect(category._page.url)
    else:
        initial_data = {
            'name': category.name,
            'description': category.description
        }
        form = InventoryCategoryForm(initial=initial_data)
    
    return render(request, 'inventory/category/update.html', {'form': form, 'category': category})

@login_required
def delete_category_view(request, user_slug, category_slug):
    user = get_object_or_404(User, slug=user_slug)
    
    if request.method == 'POST':
        form = InventoryCategoryDeletionForm(request.POST)
        if form.is_valid():
            fullslug = f"{user_slug}/{category_slug}"
            category = get_object_or_404(apps.get_model('inventory', 'Category'), slug=fullslug)
            _name = category.name
            category.delete()
            messages.success(request, f'Category {_name} successfully deleted')
            return redirect(user.page.url)
    else:
        form = InventoryCategoryDeletionForm()
    
    return render(request, 'inventory/category/delete.html', {'form': form})
