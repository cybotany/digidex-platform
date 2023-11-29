from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from apps.inventory.models import Link
from apps.core.models import Digit
from django.core.exceptions import PermissionDenied
import hashlib


class LinkView(LoginRequiredMixin, View):
    login_url = 'core:login'

    def get(self, request, secret):
        # Hash the received secret
        secret_hash = hashlib.sha256(secret.encode()).hexdigest()

        # Retrieve the link using the hashed secret
        link = get_object_or_404(Link, secret_hash=secret_hash)

        if link.active:
            try:
                digit = Digit.objects.get(link=link)
                return redirect(reverse('core:digit_detail', kwargs={'pk': digit.pk}))
            except Digit.DoesNotExist:
                raise PermissionDenied("This link is active but not associated with a digitized plant.")
        else:
            request.session['link_id'] = str(link.id)
            return redirect(reverse('core:digitize_plant'))
