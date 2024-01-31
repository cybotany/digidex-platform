from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from digidex.utils.helpers import BaseNFCView
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm


class DigitCreationView(BaseNFCView, CreateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit-creation-page.html'

    def form_valid(self, form):
        nfc = self.get_object()

        if not nfc.active:
            form.instance.nfc_link = nfc
            return super().form_valid(form)
        # Handle cases where NFC is already active

    def form_invalid(self, form):
        # Render the template with the invalid form.
        return render(self.request, self.template_name, {'form': form})
