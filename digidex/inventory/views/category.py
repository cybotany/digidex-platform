from django.apps import apps
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from inventory.forms import CategoryForm, CategoryDeletionForm


User = get_user_model()

@login_required
def add_category_view(request, user_slug):
    user = get_object_or_404(User, slug=user_slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = user
            category.save()
            messages.success(request, f'{category.name} successfully added.')
            return redirect(category._page.url)
    else:
        form = CategoryForm()
    
    return render(request, 'inventory/category/add.html', {'form': form})

@login_required
def update_category_view(request, user_slug, category_slug):
    category = get_object_or_404(apps.get_model('Inventory', 'Category'), slug=category_slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            updated_category = form.save()
            messages.success(request, f'{updated_category.name} successfully updated')
            return redirect(updated_category._page.url)
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'inventory/category/update.html', {'form': form})


@login_required
def delete_category_view(request, user_slug, category_slug):
    if request.method == 'POST':
        form = CategoryDeletionForm(request.POST)
        if form.is_valid():
            category = get_object_or_404(apps.get_model('Inventory', 'Category'), slug=category_slug)
            _name = category.name
            category.delete()
            messages.success(request, f'Category {_name} successfully deleted')
            return redirect(reverse('home'))
    else:
        form = CategoryDeletionForm()
    
    return render(request, 'inventory/category/delete.html', {'form': form})
