from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.link.models import NTAG
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

class NTAGLinkView(LoginRequiredMixin, View):
    def get_object(self):
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            raise Http404("No serial number provided")
        return get_object_or_404(NTAG, serial_number=serial_number)

    def get(self, request, *args, **kwargs):
        ntag = self.get_object()
        # Check if NTAG is active and has an associated digit
        if ntag.active and hasattr(ntag, 'digit'):
            # Check if the current user is the user associated with the NTAG
            if ntag.user == request.user:
                # Redirect to the private digit details page
                return redirect('inventory:digit-details', uuid=ntag.digit.uuid)
            else:
                raise PermissionDenied("You do not have permission to view this digit.")
        # If NTAG is not active or doesn't have an associated digit, proceed with digit creation
        form = DigitForm()
        return render(request, 'inventory/digit-creation-page.html', {'form': form, 'ntag': ntag})

    def post(self, request, *args, **kwargs):
        ntag = self.get_object()
        form = DigitForm(request.POST)
        if form.is_valid():
            digit = Digit.create_digit(form.cleaned_data, ntag, request.user)
            messages.success(request, "Digit created successfully.")
            return HttpResponseRedirect(digit.get_absolute_url())
        else:
            messages.error(request, "There was a problem with the form. Please check the details you entered.")
            return render(request, 'inventory/digit-creation-page.html', {'form': form, 'ntag': ntag})