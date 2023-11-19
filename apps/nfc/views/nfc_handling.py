from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from apps.botany.models import Plant
from apps.nfc.models import Tag


class HandleNFCView(LoginRequiredMixin, View):
    login_url = 'accounts:login'

    def get(self, request, nfc_sn):
        logged_in_user = request.user
        tag, created = Tag.objects.get_or_create(
            serial_number=nfc_sn, 
            defaults={
                'created_by': logged_in_user,
                'active': True
            }
        )

        if created:
            pass
        else:
            tag.increment_view_count()

        try:
            plant = Plant.objects.get(nfc_tag=tag)
            return redirect('botany:describe_plant', pk=plant.id)
        except Plant.DoesNotExist:
            request.session['nfc_tag'] = nfc_sn
            return redirect('botany:register_plant')
