from django.apps import apps
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from journal.forms import JournalEntryForm

User = get_user_model()


@login_required
def journal_form_view(request, profile_slug, digit_slug):
    page_owner = get_object_or_404(User, username=profile_slug)
    requesting_user = request.user

    if page_owner != requesting_user:
        return HttpResponseForbidden("You are not allowed to edit this profile.")


    if request.method == 'POST':
        form = JournalEntryForm(request.POST, request.FILES)
        if form.is_valid():
            UserDigit = apps.get_model('digitization', 'UserDigit')
            digit = get_object_or_404(UserDigit, slug=digit_slug)
            digit_note = form.save(digit, commit=True)
            return redirect(digit_note.digit_detail_page_url)
    else:
        form = JournalEntryForm()

    return render(request, "journal/record_journal_entry.html", {'form': form})
