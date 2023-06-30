from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Prefetch

from apps.botany.models import Label, Plant


class PlantHomepageView(LoginRequiredMixin, TemplateView):
    """
    View for rendering the plant module homepage.
    """
    template_name = 'botany/homepage.html'

    def get_plant_groups_for_user(self):
        """
        Return the plants grouped by label for the currently logged-in user.
        """
        plants_prefetch = Prefetch('plants', queryset=Plant.objects.filter(user=self.request.user))
        return Label.objects.filter(user=self.request.user).prefetch_related(plants_prefetch)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plant_groups'] = self.get_plant_groups_for_user()
        return context
