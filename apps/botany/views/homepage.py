from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.botany.models import Plant, Label


class PlantHomepageView(LoginRequiredMixin, TemplateView):
    """
    View for rendering the plant module homepage.
    """
    template_name = 'botany/homepage.html'

    def get_plant_groups_for_user(self):
        """
        Return the plants grouped by label for the currently logged-in user.
        """
        labels = Label.objects.filter(user=self.request.user)
        plant_groups = []

        for label in labels:
            plants = Plant.objects.filter(label=label, label__user=self.request.user)
            plant_groups.append({
                'name': label.name,
                'plants': plants
            })

        return plant_groups

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plant_groups'] = self.get_plant_groups_for_user()
        return context
