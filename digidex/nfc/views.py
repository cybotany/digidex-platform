from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from nfc.models import NearFieldCommunicationTag
from inventory.models import DigitRegistrationFormPage

def handle_common_exceptions(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)
        except NearFieldCommunicationTag.DoesNotExist:
            messages.error(request, "NTAG not found.")
            return redirect('error_page_url')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('error_page_url')
    return wrapper

@handle_common_exceptions
def view_ntag(request, serial_number):
    try:
        ntag = NearFieldCommunicationTag.objects.get(serial_number=serial_number)
        if not ntag.digit:
            messages.info(request, "No digit is associated with this NTAG. Please create one. You will be prompted to login if you are not already.")
            return redirect('create_digit_view', serial_number=serial_number)
        url = ntag.get_digit_page_url()
        return redirect(url)
    except ValidationError as e:
        return HttpResponse(str(e), status=400)

@login_required
def link_ntag(request, serial_number):
    try:
        ntag = NearFieldCommunicationTag.objects.get(serial_number=serial_number)
        if ntag.digit:
            messages.info(request, "A digit is already associated with this NTAG.")
            return redirect(ntag.get_digit_page_url())

        form_page = DigitRegistrationFormPage.objects.first()
        if not form_page:
            messages.error(request, "Digit registration form page not found.")
            return redirect('error_page_url')

        query_string = f"serial_number={serial_number}"
        form_url = f"{form_page.url}?{query_string}"
        return redirect(form_url)

    except NearFieldCommunicationTag.DoesNotExist:
        messages.error(request, "NTAG not found.")
        return redirect('error_page_url')
