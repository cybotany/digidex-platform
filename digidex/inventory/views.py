from django.apps import apps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from inventory.forms import UserDigitizedObjectForm, UserDigitizedObjectNoteForm
from inventory.models import UserDigitizedObject


@login_required
def link_ntag_and_digit(request, profile_slug, ntag_uuid):
    UserProfile = apps.get_model('profiles', 'UserProfile')
    user_profile = get_object_or_404(UserProfile, slug=profile_slug)

    requesting_user = request.user
    if requesting_user != user_profile.user:
        requesting_user_page = requesting_user.profile.get_profile_page()
        return redirect(requesting_user_page.url)

    if request.method == 'POST':
        form = UserDigitizedObjectForm(request.POST)
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
        form = UserDigitizedObjectForm()

    return render(request, "inventory/link_ntag_and_digit.html", {'form': form})


@login_required
def add_digit_note(request, profile_slug, digit_uuid):
    UserProfile = apps.get_model('profiles', 'UserProfile')
    user_profile = get_object_or_404(UserProfile, slug=profile_slug)

    requesting_user = request.user
    if requesting_user != user_profile.user:
        requesting_user_profile_page = requesting_user.profile.get_profile_page() 
        redirect(requesting_user_profile_page.url)

    if request.method == 'POST':
        form = UserDigitizedObjectNoteForm(request.POST, request.FILES)
        if form.is_valid():
            digitized_object = get_object_or_404(UserDigitizedObject, uuid=digit_uuid)
            digitized_object_note = form.save(digitized_object, commit=True)
            return redirect(digitized_object_note.digit_detail_page_url)
    else:
        form = UserDigitizedObjectNoteForm()

    return render(request, "inventory/add_digit_note.html", {'form': form})
