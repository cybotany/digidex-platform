from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from apps.inventory.models import Link
from apps.core.models import Digit
from django.core.exceptions import PermissionDenied


class LinkingView(LoginRequiredMixin, View):
    login_url = 'core:login'

    def get(self, request, serial_number):
        link, created = Link.objects.get_or_create(serial_number=serial_number)

        if link.active and link.digit:
            digit_detail_url = link.get_digit_url()
            return redirect(digit_detail_url)
        else:
            return redirect('core:digitization', link_id=str(link.id))
