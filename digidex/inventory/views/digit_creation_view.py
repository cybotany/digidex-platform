from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm
from digidex.link.models import NFC


class DigitCreationView(LoginRequiredMixin, SingleObjectMixin, View):
    model = NFC
    template_name = 'inventory/digit-creation-page.html'

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        serial_number = self.kwargs.get('serial_number')
        if serial_number is None:
            raise Http404("No serial number provided")
        try:
            obj = queryset.get(serial_number=serial_number)
        except queryset.model.DoesNotExist:
            raise Http404("No NFC found matching the query")
        return obj

    def get(self, request, *args, **kwargs):
        nfc = self.get_object()
        form = DigitForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
            # Process the form data for a POST request
            nfc = self.get_object()
            form = DigitForm(request.POST)
            if form.is_valid():
                digit = Digit.create_digit(form.cleaned_data, nfc, request.user)
                return reverse_lazy('inventory:digit-details', serial_number=nfc.serial_number)
            else:
                # If the form is invalid, render the form with errors
                return render(self.request, self.template_name, {'form': form})
