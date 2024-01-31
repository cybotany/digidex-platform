from django.http import Http404
from digidex.link.views.base_nfc_view import BaseNFCView
from digidex.inventory.models import Digit


class BaseDigitView(BaseNFCView):
    model = Digit

    def get_object(self, queryset=None):
        # First, get the NFC object using the superclass's get_object method
        nfc = super().get_object(queryset=queryset)

        # Then, retrieve the associated Digit using the NFC object
        try:
            return Digit.objects.get(nfc_link=nfc)
        except Digit.DoesNotExist:
            raise Http404("No Digit found for the given NFC link")
