import requests

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from nfc.models import NearFieldCommunicationTag

def view_ntag(request, serial_number):
    try:
        ntag = NearFieldCommunicationTag.objects.get(serial_number=serial_number)
        url = ntag.get_digit_page_url()
        return redirect(url)
    except NearFieldCommunicationTag.DoesNotExist:
        return HttpResponse("NTAG not found", status=404)
    except ValidationError as e:
        return HttpResponse(str(e), status=400)


def create_digit(self, user):
    if self.digit:
        return {'status': 'error', 'message': "There's already an associated digit for this tag."}

    api_url = 'http://example.com/api/create-digit'
    try:
        response = requests.post(
            api_url,
            data={
                'user_id': user.id,
                'serial_number': self.serial_number
            }
        )
        if response.status_code == 302:
            return {'status': 'success', 'redirect_url': response.json().get('redirect_url')}
        else:
            return {'status': 'error', 'message': "Unable to process the digit registration."}
    except requests.RequestException as e:
        return {'status': 'error', 'message': str(e)}
