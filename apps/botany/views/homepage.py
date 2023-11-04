from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.botany.models import Plant, Group


class PlantHomepageView(LoginRequiredMixin, TemplateView):
    """
    View for rendering the plant module homepage.
    """
    template_name = 'botany/homepage.html'

    def get_plants_for_group(self):
        """
        Return all plants for the currently logged-in user in the default group.
        """
        default_group = Group.objects.get(user=self.request.user, position=1)
        return Plant.objects.filter(user=self.request.user, group=default_group).order_by('added_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plants'] = self.get_plants_for_group()
        return context
