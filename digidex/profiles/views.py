from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model

from profiles.forms import UserProfileForm

User = get_user_model()


@login_required
def profile_form_view(request, profile_slug):
    page_owner = get_object_or_404(User, username=profile_slug)
    requesting_user = request.user

    if page_owner != requesting_user:
        return HttpResponseForbidden("You are not allowed to edit this profile.")

    user_profile = page_owner.profile
    user_profile_page = user_profile.get_profile_page()

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect(user_profile_page.url)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/user_profile_form.html', {'form': form})
