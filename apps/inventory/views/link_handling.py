from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from apps.inventory.models import Link
from django.core.exceptions import PermissionDenied


class HandleLinkView(LoginRequiredMixin, View):
    login_url = 'accounts:login'

    def get(self, request, link_sn):
        link = get_object_or_404(Link, serial_number=link_sn)

        if link.active:
            pass
        else:
            request.session['link_id'] = str(link.id)
            pass
