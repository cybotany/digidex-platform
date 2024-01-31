from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm
from digidex.link.models import NFC


class DigitCreationView(CreateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit-creation-page.html'

    def form_valid(self, form):
        serial_number = self.kwargs.get('serial_number')
        nfc = get_object_or_404(NFC, serial_number=serial_number)
        digit = Digit.create_digit(form.cleaned_data, nfc, self.request.user)
        return redirect('inventory:digit-details', serial_number=nfc.serial_number)

    def form_invalid(self, form):
        # Render the template with the invalid form.
        return render(self.request, self.template_name, {'form': form})
