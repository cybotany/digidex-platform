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
            return redirect('link-ntag', uuid=_uuid)
        url = ntag.get_digit_page_url()
        return redirect(url)
    except ValidationError as e:
        return HttpResponse(str(e), status=400)

@login_required
def link_ntag(request, uuid):
    ntag = get_object_or_404(NearFieldCommunicationTag, uuid=uuid)

    if request.method == 'POST':
        form = DigitizedObjectForm(request.POST)
        if form.is_valid():
            digit = form.save(commit=False)
            digit.save()
            ntag.digit = digit
            ntag.save()
            messages.success(request, "Digitized object has been successfully linked.")
            return redirect('success_url')
        else:
            messages.error(request, "There were errors in your form. Please correct them.")
    else:
        form = DigitizedObjectForm()

    return render(request, 'digitized_object/create.html', {'form': form, 'uuid': uuid})
