from django.views.generic import DetailView
from apps.botany.models import Plant


class DescribePlantView(DetailView):
    """
    View for rendering the page used to show details about a specific registered plant.
    """
    model = Plant
    template_name = 'botany/describe_plant.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['watering_events'] = self.object.waterings.all().order_by('-timestamp')
        return context
