from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from accounts.forms import UserProfileForm

User = get_user_model()


@login_required
def profile_form_view(request, user_slug):
    page_owner = get_object_or_404(User, username=user_slug)
    requesting_user = request.user

    if page_owner != requesting_user:
        return HttpResponseForbidden("You are not allowed to edit this profile.")

    user_profile = page_owner.profile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            updated_profile = form.save(commit=False)
            updated_profile.save()
            return redirect(updated_profile.page.url)
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'accounts/user_profile_update.html', {'form': form})
