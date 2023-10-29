from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.itis.models import Kingdoms


class ITISHomepageView(LoginRequiredMixin, TemplateView):
    """
    View for rendering the plant module homepage.
    """
    template_name = 'itis/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kingdoms'] = Kingdoms.objects.all()
        return context
