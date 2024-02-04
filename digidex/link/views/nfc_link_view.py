from django.shortcuts import redirect
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from digidex.link.models import NFC

class NFCLinkView(LoginRequiredMixin, SingleObjectMixin, View):
    model = NFC

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            raise Http404("No serial number provided")
        return get_object_or_404(queryset, serial_number=serial_number)

    def get(self, request, *args, **kwargs):
        nfc = self.get_object()
        # Check if NFC is active and has an associated digit
        if nfc.active and hasattr(nfc, 'digit'):
            # Check if the current user is the user associated with the NFC tag
            if nfc.user == request.user:
                # Redirect to the private digit details page
                return redirect('inventory:digit-details', uuid=nfc.digit.uuid)
            else:
                # Redirect to the public digit page
                return redirect('inventory:public-digit', uuid=nfc.digit.uuid)
        # If NFC is not active or doesn't have an associated digit, proceed with digit creation
        return redirect('inventory:digit-creation', serial_number=nfc.serial_number)
