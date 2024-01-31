from django.views import View
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404
from digidex.link.models import NFC
from digidex.inventory.models import Digit


class BaseNFCView(LoginRequiredMixin, SingleObjectMixin, View):
    model = NFC

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            raise Http404("No serial number provided")
        return get_object_or_404(queryset, serial_number=serial_number)



    class BaseDigitView(BaseNFCView):
        model = Digit

        def get_object(self, queryset=None):
            serial_number = self.kwargs.get('serial_number')
            if not serial_number:
                raise Http404("No serial number provided")
            nfc = get_object_or_404(NFC, serial_number=serial_number)

            try:
                return Digit.objects.get(nfc_link=nfc)
            except Digit.DoesNotExist:
                raise Http404("No Digit found for the given NFC link")
