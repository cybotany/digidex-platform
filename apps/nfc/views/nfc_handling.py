from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.core.exceptions import MultipleObjectsReturned
from django.views import View
from apps.botany.models import Plant


class HandleNFCView(LoginRequiredMixin, View):
    login_url = 'accounts:login'
    redirect_field_name = 'next'

    def get(self, request, nfc_sn):
        try:
            plant = get_object_or_404(Plant, nfc_tag=nfc_sn)
            return redirect('botany:describe_plant', pk=plant.id)
        except MultipleObjectsReturned:
            # Handle the case where multiple objects are returned
            return redirect('some_error_page')
        except Plant.DoesNotExist:
            # Redirect to the plant registration page with the NFC tag
            return redirect('botany:register_plant_nfc', nfc_tag=nfc_sn)
