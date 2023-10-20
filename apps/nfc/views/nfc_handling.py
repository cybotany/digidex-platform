from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from apps.botany.models import Plant
from apps.nfc.models import Tag


class HandleNFCView(LoginRequiredMixin, View):
    login_url = 'accounts:login'

    def get(self, request, nfc_sn):
        # Get or create the NFC Tag
        tag, created = Tag.objects.get_or_create(serial_number=nfc_sn)
        
        if created:
            # Handle the case where the Tag was newly created, if needed
            pass

        try:
            plant = Plant.objects.get(nfc_tag=tag) # Adjust the query if `nfc_tag` is not the field linking Plant to Tag
            return redirect('botany:describe_plant', pk=plant.id)
        except Plant.DoesNotExist:
            request.session['nfc_tag'] = nfc_sn
            return redirect('botany:register_plant')
