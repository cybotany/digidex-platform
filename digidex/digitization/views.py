from django.apps import apps
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model

from digitization.forms import DigitalObjectForm

User = get_user_model()


@login_required
def link_ntag(request, ntag_uuid):
    if request.method == 'POST':
        form = DigitalObjectForm(request.POST, user=request.user)
        if form.is_valid():
            digitized_object = form.save()
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
        form = DigitalObjectForm(user=request.user)

    return render(request, "digitization/link_ntag.html", {'form': form})
