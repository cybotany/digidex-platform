from django.views.generic import DetailView
from ..models import Plant


class PlantDetail(DetailView):
    model = Plant
    template_name = 'botany/plant_detail.html'
