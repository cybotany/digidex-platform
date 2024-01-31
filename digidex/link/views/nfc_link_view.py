from django.shortcuts import redirect
from digidex.link.views import BaseNFCView
from digidex.link.models import NFC


class NFCLinkView(BaseNFCView):
    model = NFC
    
    def get(self, request, *args, **kwargs):
        nfc = self.get_object()
        if not nfc.active:
            return redirect('inventory:digit-creation', serial_number=self.object.serial_number)
        return redirect('inventory:digit-details', serial_number=self.object.serial_number)
