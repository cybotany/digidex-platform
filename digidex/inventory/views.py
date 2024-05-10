from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from nfc.models import NearFieldCommunicationTag
from inventory.forms import UserDigitizedObjectForm, UserDigitizedObjectNoteForm
from inventory.models import UserDigitizedObject


@login_required
def link_ntag_and_digit(request, ntag_uuid):
    if request.method == 'POST':
        form = UserDigitizedObjectForm(request.POST)
        if form.is_valid():
            digitized_object = form.save(request.user.profile, commit=True)
            ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
            ntag.digitized_object = digitized_object
            ntag.save()
            digitized_object_page = digitized_object.detail_page
            return redirect(digitized_object_page.url)
    else:
        form = UserDigitizedObjectForm()

    return render(request, "inventory/link_ntag_and_digit.html", {'form': form})


@login_required
def add_digit_note(request, digit_uuid):
    digitized_object = get_object_or_404(UserDigitizedObject, uuid=digit_uuid)

    if request.method == 'POST':
        form = UserDigitizedObjectNoteForm(request.POST, request.FILES)
        if form.is_valid():
            digitized_object_note = form.save(digitized_object, commit=True)
            return redirect(digitized_object_note.digit_detail_page_url)
    else:
        form = UserDigitizedObjectNoteForm()

    return render(request, "inventory/add_digit_note.html", {'form': form})
