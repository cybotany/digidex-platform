from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView
from digidex.utils.helpers import BaseNFCView
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm


class DigitCreationView(BaseNFCView, CreateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit-creation-page.html'

    def form_valid(self, form):
        self.object = form.save()
        return reverse_lazy('inventory:digit-details', kwargs={'serial_number': self.object.nfc_link.serial_number})

    def form_invalid(self, form):
        # Render the template with the invalid form.
        return render(self.request, self.template_name, {'form': form})
