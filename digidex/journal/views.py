from django.apps import apps
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from digitization.models import UserDigit


@login_required
def add_digit_note(request, profile_slug, digit_uuid):
    UserProfile = apps.get_model('profiles', 'UserProfile')
    user_profile = get_object_or_404(UserProfile, slug=profile_slug)

    requesting_user = request.user
    if requesting_user != user_profile.user:
        requesting_user_profile_page = requesting_user.profile.get_profile_page() 
        redirect(requesting_user_profile_page.url)

    if request.method == 'POST':
        form = JournalEntryForm(request.POST, request.FILES)
        if form.is_valid():
            digitized_object = get_object_or_404(UserDigit, uuid=digit_uuid)
            digitized_object_note = form.save(digitized_object, commit=True)
            return redirect(digitized_object_note.digit_detail_page_url)
    else:
        form = JournalEntryForm()

    return render(request, "inventory/add_digit_note.html", {'form': form})
