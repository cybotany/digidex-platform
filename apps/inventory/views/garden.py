from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.models import Digit


class GardenView(LoginRequiredMixin, ListView):
    model = Digit
    context_object_name = 'digits'
    template_name = 'inventory/garden.html'

    def get_queryset(self):
        """ Overriding to get Digits for the current user """
        return Digit.objects.filter(user=self.request.user)
