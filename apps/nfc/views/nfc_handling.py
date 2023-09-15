from django.shortcuts import redirect
from django.views import View
from apps.botany.models import Plant


class HandleNFCView(View):
    def get(self, request, nfc_sn):
        try:
            plant = Plant.objects.get(nfc_tag=nfc_sn)
            return redirect('plant_detail_view', plant_id=plant.id)  # Assuming you have a detail view for plants.
        except Plant.DoesNotExist:
            # If the NFC tag isn't associated with any plant
            return redirect('plant_registration_form', nfc_tag=nfc_sn)
