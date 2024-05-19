from django.apps import apps
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from journal.forms import JournalEntryForm

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
            UserDigit = apps.get_model('digitization', 'UserDigit')
            digit = get_object_or_404(UserDigit, uuid=digit_uuid)
            digit_note = form.save(digit, commit=True)
            return redirect(digit_note.digit_detail_page_url)
    else:
        form = JournalEntryForm()

    return render(request, "journal/record_journal_entry.html", {'form': form})
