from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.models import Link
from apps.core.models import Digit


class GardenView(LoginRequiredMixin, ListView):
    model = Digit
    context_object_name = 'digits'
    template_name = 'garden.html'

    def get_queryset(self):
        """ Overriding to get Digits for the current user """
        link_pks = Link.objects.filter(user=self.request.user, active=True).values_list('digit', flat=True)
        return Digit.objects.filter(pk__in=link_pks)
