from django.shortcuts import render, redirect
from digidex.utils.helpers import BaseNFCView
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm


class DigitCreationView(BaseNFCView):
    template_name = 'inventory/digit-creation-page.html'

    def get(self, request, *args, **kwargs):
        form = DigitForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
            # Process the form data for a POST request
            form = DigitForm(request.POST)
            if form.is_valid():
                nfc = self.get_object()
                # Use the custom creation method from the Digit model
                digit = Digit.create_digit(form.cleaned_data, nfc, request.user)
                # Redirect to the success URL after creating the digit
                return redirect('inventory:digit-details', serial_number=nfc.serial_number)
            else:
                # If the form is invalid, render the form with errors
                return render(self.request, self.template_name, {'form': form})
