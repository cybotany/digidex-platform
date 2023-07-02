from django.views.generic import DetailView
from apps.botany.models import Plant


class DescribePlantView(DetailView):
    """
    View for rendering the page used to show details about a specific registered plant.
    """
    model = Plant
    template_name = 'botany/describe_plant.html'
