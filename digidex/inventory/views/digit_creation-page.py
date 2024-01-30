from django.http import HttpResponseRedirect
from django.shortcuts import render
from digidex.link.views import BaseNFCLinkedView
from digidex.inventory.forms import DigitForm


class DigitCreationView(BaseNFCLinkedView):
    def post(self, request, *args, **kwargs):
        nfc = self.get_object()
        if not nfc.active:
            form = DigitForm(request.POST, request.FILES)
            if form.is_valid():
                digit = form.save(commit=False)
                digit.nfc_link = nfc
                digit.save()
                # Redirect to the digit details page or another appropriate page
                return HttpResponseRedirect('/path-to-redirect-after-creation/')
            else:
                # Render the page again with form errors
                return render(request, 'inventory/digit-creation-page.html', {'form': form})
        else:
            # Handle cases where NFC is already active
            # You might want to redirect or show an error message
            return HttpResponseRedirect('/path-to-redirect-if-nfc-active/')
