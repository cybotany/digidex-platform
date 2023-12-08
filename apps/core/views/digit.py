from django.views.generic import DetailView
from apps.core.models import Digit


class DigitView(DetailView):
    """
    View for rendering the page used to show details about a specific registered digit.
    """
    model = Digit
    template_name = 'digit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['watering_events'] = self.object.waterings.all().order_by('-timestamp')
        context['fertilization_events'] = self.object.fertilizations.all().order_by('-timestamp')
        return context