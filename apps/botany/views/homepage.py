from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.botany.models import Label


class PlantHomepageView(LoginRequiredMixin, TemplateView):
    """
    View for rendering the plant module homepage.
    """
    template_name = 'botany/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plant_groups'] = self.get_plant_groups_for_user()
        return context

    def get_plant_groups_for_user(self):
        """
        Return the plants grouped by label for the currently logged-in user.
        """
        return list(
            Label.objects.filter(
                user=self.request.user,
                plant__isnull=False,
                plant__owner=self.request.user
            )
            .distinct()
            .prefetch_related('plant_set')
        )
