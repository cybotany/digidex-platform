from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from apps.nfc.models import Link
from apps.inventory.models import Digit


class LinkingView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        link_uuid = kwargs.get('uuid')

        if not link_uuid:
            return HttpResponse("No PK provided", status=400)

        link = get_object_or_404(Link, uuid=link_uuid)
        link.counter += 1
        link.save()

        if not link.active:
            return redirect('inventory:creation', uuid=link_uuid)
        else:
            if request.user == link.user:
                digit = get_object_or_404(Digit, nfc_link=link)
                return redirect('inventory:details', uuid=link_uuid)
            else:
                return HttpResponse("Unauthorized access", status=403)
