from django.shortcuts import redirect, render, get_object_or_404, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from nfc.models import NearFieldCommunicationTag
from digitization.forms import DigitizedObjectForm, DigitizedObjectImageForm
from digitization.models import DigitizedObject

@login_required
def link_ntag_and_digit(request, ntag_uuid):
    if request.method == 'POST':
        form = DigitizedObjectForm(request.POST)
        if form.is_valid():
            _digitized_object = form.save()
            ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
            ntag.digitized_object = _digitized_object
            ntag.save()
            return redirect('digitization:link_user', digit_uuid=_digitized_object.uuid)
    else:
        form = DigitizedObjectForm()

    return render(request, "digitization/link_ntag_and_digit.html", {'form': form})

@login_required
def link_digit_and_user(request, digit_uuid):
    _digitized_object = get_object_or_404(DigitizedObject, uuid=digit_uuid)
    _user_digit = _digitized_object.set_user_association(request.user)
    _user_digit.save()
    _user_digit_page = _user_digit.create_digit_page()

    if not _user_digit_page:
        raise Http404("User Digitized Object Page could not be created.")
    redirect(_user_digit_page.url)


@login_required
def link_digit_and_image(request, digit_uuid):
    _digitized_object = get_object_or_404(DigitizedObject, uuid=digit_uuid)

    if request.method == 'POST':
        form = DigitizedObjectImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_obj = form.save(commit=False)
            image_obj.digit = _digitized_object
            image_obj.save()
            _user_digit_page_url = _digitized_object.get_associated_page_url()
            return redirect('some_success_url')
    else:
        form = DigitizedObjectImageForm()

    return render(request, "digitization/link_digit_and_image.html", {'form': form})
