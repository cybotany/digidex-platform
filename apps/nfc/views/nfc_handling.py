from django.shortcuts import redirect
from django.views import View
from apps.botany.models import Plant


class HandleNFCView(View):
    def get(self, request, nfc_sn):
        try:
            plant = Plant.objects.get(nfc_tag=nfc_sn)
            return redirect('botany:describe_plant', pk=plant.id)
        except Plant.DoesNotExist:
            return redirect('botany:register_plant')
