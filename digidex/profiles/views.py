from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model

from profiles.forms import UserProfileForm

User = get_user_model()

@login_required
def update_user_profile_view(request, user_slug):
    profile_owner = get_object_or_404(User, username=user_slug)
    requesting_user = request.user

    if profile_owner != requesting_user:
        return HttpResponseForbidden("You are not allowed to edit this profile.")

    user_profile = profile_owner.profile
    page = user_profile.create_profile_page()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = requesting_user
            new_profile.save()
            return redirect(page)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/user_profile_form.html', {'form': form})
