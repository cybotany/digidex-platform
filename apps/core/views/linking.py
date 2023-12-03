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
        # Retrieve the link using the serial_number
        link, created = Link.objects.get_or_create(serial_number=serial_number)

        if link.active:
            try:
                digit = Digit.objects.get(link=link)
                return redirect(reverse('core:digit_detail', kwargs={'pk': digit.pk}))
            except Digit.DoesNotExist:
                raise PermissionDenied("This link is active but not associated with a digit.")
        else:
            request.session['link_id'] = str(link.id)
            return redirect(reverse('core:digitize'))
