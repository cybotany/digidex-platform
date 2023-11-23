from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from apps.nfc.models import Tag
from django.core.exceptions import PermissionDenied


class HandleNFCView(LoginRequiredMixin, View):
    login_url = 'accounts:login'

    def get(self, request, nfc_sn):
        tag = get_object_or_404(Tag, serial_number=nfc_sn)

        # Check if the tag is active and has an associated plant
        if tag.active and tag.plant:
            return redirect('botany:describe_plant', pk=tag.plant.id)
        elif tag.active and not tag.plant:
            # Handle the case where the tag is active but not linked to any plant
            raise PermissionDenied("Tag is active but not associated with any plant.")
        else:
            # If the tag is inactive, store the tag's UUID in the session
            request.session['nfc_uuid'] = str(tag.uuid)
            return redirect('botany:register_plant')
