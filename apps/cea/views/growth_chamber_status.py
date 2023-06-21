from django.views.generic.detail import DetailView
from apps.cea.models import GrowthChamber


class GrowthChamberStatus(DetailView):
    model = GrowthChamber
    template_name = 'cea/growth_chamber_status.html'
