from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.urls import reverse

from accounts.forms import UserProfileForm, DeleteUserForm

User = get_user_model()


@login_required
def update_account_view(request, user_slug):
    page_owner = get_object_or_404(User, slug=user_slug)
    requesting_user = request.user

    if page_owner != requesting_user:
        return HttpResponseForbidden("You are not allowed to edit this profile.")

    user_profile = page_owner.profile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')
            return redirect(page_owner.page.url)
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'accounts/update_account.html', {'form': form})


@login_required
def delete_account_view(request, user_slug):
    page_owner = get_object_or_404(User, slug=user_slug)
    requesting_user = request.user

    if page_owner != requesting_user:
        return HttpResponseForbidden("You are not allowed to edit this profile.")

    if request.method == 'POST':
        form = DeleteUserForm(request.POST)
        if form.is_valid():
            logout(request)
            requesting_user.delete()
            messages.success(request, 'Account successfully deleted')
            return redirect(reverse('home'))
    else:
        form = DeleteUserForm()
    
    return render(request, 'accounts/delete_account.html', {'form': form})
    