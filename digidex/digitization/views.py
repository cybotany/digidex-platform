from django.apps import apps
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model

from digitization.forms import UserDigitForm

User = get_user_model()


@login_required
def create_digit_with_ntag(request, ntag_uuid):
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
