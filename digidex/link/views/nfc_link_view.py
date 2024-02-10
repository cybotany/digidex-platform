from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.link.models import NFC
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

class NFCLinkView(LoginRequiredMixin, View):
    def get_object(self):
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            raise Http404("No serial number provided")
        return get_object_or_404(NFC, serial_number=serial_number)

    def get(self, request, *args, **kwargs):
        nfc = self.get_object()
        # Check if NFC is active and has an associated digit
        if nfc.active and hasattr(nfc, 'digit'):
            # Check if the current user is the user associated with the NFC tag
            if nfc.user == request.user:
                # Redirect to the private digit details page
                return redirect('inventory:digit-details', uuid=nfc.digit.uuid)
            else:
                # Redirect to the public digit page
                return redirect('inventory:public-digit', uuid=nfc.digit.uuid)
        # If NFC is not active or doesn't have an associated digit, proceed with digit creation
        form = DigitForm()
        return render(request, 'inventory/digit-creation-page.html', {'form': form, 'nfc': nfc})

    def post(self, request, *args, **kwargs):
        nfc = self.get_object()
        form = DigitForm(request.POST)
        if form.is_valid():
            digit = Digit.create_digit(form.cleaned_data, nfc, request.user)
            messages.success(request, "Digit created successfully.")
            return HttpResponseRedirect(digit.get_absolute_url())
        else:
            messages.error(request, "There was a problem with the form. Please check the details you entered.")
            return render(request, 'inventory/digit-creation-page.html', {'form': form, 'nfc': nfc})