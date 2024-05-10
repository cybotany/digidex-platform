from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from nfc.models import NearFieldCommunicationTag
from inventory.forms import UserDigitizedObjectForm, UserDigitizedObjectJournalForm
from inventory.models import UserDigitizedObject


@login_required
def link_ntag_and_digit(request, ntag_uuid):
    user_profile = request.user.profile
    if request.method == 'POST':
        form = UserDigitizedObjectForm(request.POST)
        if form.is_valid():
            digitized_object = form.save(user_profile, commit=True)
            ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
            ntag.digitized_object = digitized_object
            ntag.save()
            return redirect(digitized_object.get_associated_page_url())
    else:
        form = UserDigitizedObjectForm()

    return render(request, "digitization/link_ntag_and_digit.html", {'form': form})

@login_required
def link_digit_and_journal(request, digit_uuid):
    digitized_object = get_object_or_404(UserDigitizedObject, uuid=digit_uuid)

    if request.method == 'POST':
        form = UserDigitizedObjectJournalForm(request.POST, request.FILES)
        if form.is_valid():
            journal_entry = form.save(digitized_object, commit=True)
            return redirect(journal_entry.get_associated_page_url())
    else:
        form = UserDigitizedObjectJournalForm()

    return render(request, "digitization/link_digit_and_journal.html", {'form': form})
