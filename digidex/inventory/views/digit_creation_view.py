from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from digidex.utils.helpers import BaseNFCView
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm


class DigitCreationView(BaseNFCView, CreateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit-creation-page.html'

    def form_valid(self, form):
        self.object = form.save()
        return super(DigitCreationView, self).form_valid(form)

    def form_invalid(self, form):
        # Render the template with the invalid form.
        return render(self.request, self.template_name, {'form': form})

    def get_success_url(self):
        """
        Returns the URL to redirect to after successfully creating a digit.
        This URL is constructed based on the digit's associated NFC's serial number.
        """
        # Ensure that self.object is set before calling this method
        return reverse_lazy('inventory:digit-details', kwargs={'serial_number': self.object.nfc_link.serial_number})