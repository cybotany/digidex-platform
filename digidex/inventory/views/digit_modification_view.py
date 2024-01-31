from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from digidex.utils.helpers import BaseDigitView
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm


class DigitModificationView(BaseDigitView, UpdateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit-modification-page.html'

    def get_object(self, queryset=None):
        # Use the BaseDigitView's get_object method to get the associated Digit
        return super().get_object(queryset=queryset)

    def form_valid(self, form):
        form.save()
        return redirect('inventory:digit-details', serial_number=self.object.nfc_link.serial_number)
