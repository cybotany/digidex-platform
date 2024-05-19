from django.apps import apps
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model

from profiles.forms import UserProfileForm
from digitization.forms import UserDigitForm

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
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            updated_profile = form.save(commit=False)
            # Ensure profile avatar is sized appropriately here
            updated_profile.save()
            return redirect(user_profile_page.url)
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'profiles/user_profile_update.html', {'form': form})


@login_required
def create_digit_with_ntag(request, profile_slug, ntag_uuid):
    UserProfile = apps.get_model('profiles', 'UserProfile')
    user_profile = get_object_or_404(UserProfile, slug=profile_slug)

    requesting_user = request.user
    if requesting_user != user_profile.user:
        requesting_user_page = requesting_user.profile.get_profile_page()
        return redirect(requesting_user_page.url)

    if request.method == 'POST':
        form = UserDigitForm(request.POST)
        if form.is_valid():
            digitized_object = form.save(commit=False)
            digitized_object.user_profile = user_profile

            digitized_object_page = digitized_object.create_digit_page()
            if digitized_object_page:
                NearFieldCommunicationTag = apps.get_model('nfc', 'NearFieldCommunicationTag')
                ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
                ntag.digitized_object = digitized_object
                ntag.save()
                return redirect(digitized_object_page.url)
            else:
                return HttpResponseForbidden("Failed to create a detail page for the digitized object.")
    else:
        form = UserDigitForm()

    return render(request, "digitization/create_digit_with_ntag.html", {'form': form})
