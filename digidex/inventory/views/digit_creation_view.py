from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from digidex.utils.helpers import BaseNFCView
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm


class DigitCreationView(BaseNFCView, CreateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit-creation-page.html'

    def form_valid(self, form):
        nfc = self.get_object()
        self.object = Digit.create_digit(form.cleaned_data, nfc, self.request.user)
        return redirect('inventory:digit-details', kwargs={'serial_number': nfc.serial_number})

    def form_invalid(self, form):
        # Render the template with the invalid form.
        return render(self.request, self.template_name, {'form': form})
