from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404

from nfc.models import NearFieldCommunicationTag

class LinkDigit(View):


    def get_object(self, serial_number):
        """
        Retrieves an NTAG by its serial number or raises a 404 error if not found.
        """
        if not serial_number:
            raise Http404("No serial number provided")
        return get_object_or_404(NearFieldCommunicationTag, serial_number=serial_number)

    def get(self, request, *args, **kwargs):
        serial_number = kwargs.get('serial_number')
        ntag = self.get_object(serial_number)

        if ntag.digit:
            return redirect(ntag.digit.page())

        else:
            return redirect('inventory:digit_page_list')

    def post(self, request, *args, **kwargs):
        serial_number = request.POST.get('serial_number')
        ntag = self.get_object(serial_number)
        ntag.activate_link()

        return redirect(ntag.digit_page.get_absolute_url())
