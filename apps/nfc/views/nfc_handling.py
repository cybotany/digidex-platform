from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from apps.botany.models import Plant
from apps.nfc.models import Tag
from django.core.exceptions import PermissionDenied


class HandleNFCView(LoginRequiredMixin, View):
    login_url = 'accounts:login'

    def get(self, request, nfc_sn):
        tag = get_object_or_404(Tag, serial_number=nfc_sn)

        if tag.active:
            try:
                plant = Plant.objects.get(nfc_tag=tag)
                return redirect('botany:describe_plant', pk=plant.id)
            except Plant.DoesNotExist:
                raise PermissionDenied("Tag is active but no associated plant found.")
        else:
            # Store the Tag ID in the session, so it can be used to register a plant
            request.session['nfc_tag_id'] = tag.id
            return redirect('botany:register_plant', nfc_sn=tag.serial_number)
