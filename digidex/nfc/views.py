from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from nfc.models import NearFieldCommunicationTag
from digitization.forms import DigitizedObjectForm

def view_ntag(request, _uuid):
    try:
        ntag = NearFieldCommunicationTag.objects.get(uuid=_uuid)
        if not ntag.digit:
            messages.info(request, "No digit is associated with this NTAG. Please create one. You will be prompted to login if you are not already.")
            return redirect('link-ntag', _uuid=_uuid)
        url = ntag.get_dynamic_url()
        return redirect(url)
    except ValidationError as e:
        return HttpResponse(str(e), status=400)

@login_required
def link_ntag(request, _uuid):
    if request.method == 'POST':
        form = DigitizedObjectForm(request.POST)
        if form.is_valid():
            digit = form.save()
            
            user_digit = digit.create_user_association(request.user)
            digit.save()

            ntag = get_object_or_404(NearFieldCommunicationTag, uuid=_uuid)
            ntag.digit = user_digit
            ntag.save()
            messages.success(request, "Digitized object has been successfully linked.")
            return redirect(ntag.get_dynamic_url())
        else:
            messages.error(request, "There were errors in your form. Please correct them.")
    else:
        form = DigitizedObjectForm()

    return render(request, "digitization/link_ntag.html", {'form': form})
