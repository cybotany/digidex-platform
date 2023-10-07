from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from apps.botany.models import Plant


class HandleNFCView(LoginRequiredMixin, View):
    login_url = 'accounts:login'

    def get(self, request, nfc_sn):
        try:
            plant = Plant.objects.get(nfc_tag=nfc_sn)
            return redirect('botany:describe_plant', pk=plant.id)
        except Plant.DoesNotExist:
            request.session['nfc_tag'] = nfc_sn
            return redirect('botany:register_plant')
