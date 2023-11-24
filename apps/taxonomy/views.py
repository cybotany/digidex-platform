from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.taxonomy.models import Kingdoms


class HomepageView(LoginRequiredMixin, TemplateView):
    """
    View for rendering the taxonomy module homepage.
    """
    template_name = 'taxonomy/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kingdoms'] = Kingdoms.objects.all()
        return context
