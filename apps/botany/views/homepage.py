from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.botany.models import Plant

class PlantHomepageView(LoginRequiredMixin, TemplateView):
    """
    View for rendering the plant module homepage.
    """
    template_name = 'botany/homepage.html'

    def get_plants_for_user(self):
        """
        Return all plants for the currently logged-in user.
        """
        return Plant.objects.filter(user=self.request.user).order_by('added_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plants'] = self.get_plants_for_user()
        return context
