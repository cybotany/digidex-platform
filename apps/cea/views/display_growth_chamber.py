from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import GrowthChamber


class DisplayGrowthChamber(LoginRequiredMixin, ListView):
    model = GrowthChamber
    template_name = 'cea/user_growth_chambers.html'
    context_object_name = 'growth_chambers'

    def get_queryset(self):
        return GrowthChamber.objects.filter(user=self.request.user)
