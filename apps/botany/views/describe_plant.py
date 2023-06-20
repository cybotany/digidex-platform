from django.views.generic import DetailView
from ..models import Plant


class DescribePlantView(DetailView):
    model = Plant
    template_name = 'botany/describe_plant.html'
