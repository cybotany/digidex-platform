from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm
from digidex.link.models import NFC


class DigitCreationView(LoginRequiredMixin, CreateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit-creation-page.html'

    def form_valid(self, form):
        serial_number = self.kwargs.get('serial_number')
        nfc = get_object_or_404(NFC, serial_number=serial_number)
        self.object = Digit.create_digit(form.cleaned_data, nfc, self.request.user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

    def get_success_url(self):
        """
        After successfully creating the digit, redirect to the digit's URL.
        """
        return self.object.get_absolute_url()
