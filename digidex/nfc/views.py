from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from digitization.forms import DigitizedObjectForm, DigitizedObjectImageForm
from digitization.models import DigitizedObject

from nfc.models import NearFieldCommunicationTag

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
    ntag = get_object_or_404(NearFieldCommunicationTag, uuid=_uuid)
    if ntag.digit:
        return redirect(ntag.get_dynamic_url())

    if 'digit_id' in request.session:
        digit = DigitizedObject.objects.get(id=request.session['digit_id'])
        image_form = DigitizedObjectImageForm(request.POST or None, request.FILES or None)
        if request.method == 'POST' and image_form.is_valid():
            image_instance = image_form.save(commit=False)
            image_instance.digit = digit
            image_instance.save()
            del request.session['digit_id']
            messages.success(request, "Image added successfully.")
            return redirect(ntag.get_dynamic_url())

        return render(request, "digitization/link_image.html", {'form': image_form, 'ntag': ntag})

    form = DigitizedObjectForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        digit = form.save()
        request.session['digit_id'] = digit.id
        messages.success(request, "Digitized object has been successfully linked.")
        return redirect('link_ntag', _uuid=_uuid)

    return render(request, "digitization/link_ntag.html", {'form': form})
