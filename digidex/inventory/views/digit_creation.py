from django.views import View
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404, render
from digidex.inventory.models import Digit
from digidex.link.models import NFC
from digidex.inventory.forms import DigitForm


class DigitCreationView(LoginRequiredMixin, SingleObjectMixin, View):
    model = NFC

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            raise Http404("No serial number provided")
        return get_object_or_404(queryset, serial_number=serial_number)

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
