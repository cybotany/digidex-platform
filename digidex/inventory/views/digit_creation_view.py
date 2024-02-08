from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm
from digidex.link.models import NFC
import logging

logger = logging.getLogger(__name__)

class DigitCreationView(LoginRequiredMixin, CreateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit-creation-page.html'

    def form_valid(self, form):
        serial_number = self.kwargs.get('serial_number')
        nfc = get_object_or_404(NFC, serial_number=serial_number)
        self.object = Digit.create_digit(form.cleaned_data, nfc, self.request.user)
        messages.success(self.request, "Digit created successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was a problem with the form. Please check the details you entered.")  # Optionally add error message
        return super().form_invalid(form)

    def get_success_url(self):
        """
        After successfully creating the digit, redirect to the digit's URL.
        """
        return self.object.get_absolute_url()
