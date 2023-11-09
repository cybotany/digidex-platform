from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.botany.models import Group


class PlantHomepageView(LoginRequiredMixin, TemplateView):
    """
    View for rendering the plant module homepage.
    """
    template_name = 'botany/plant_grid.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_groups = Group.objects.filter(user=self.request.user).order_by('position').all()

        current_group = user_groups.first()
        prev_group = user_groups.last() if current_group.position == 1 else user_groups[current_group.position - 2]
        next_group = user_groups.first() if current_group.position == len(user_groups) else user_groups[current_group.position]

        context['current_group'] = current_group
        context['prev_group_id'] = prev_group.id
        context['next_group_id'] = next_group.id

        return context
