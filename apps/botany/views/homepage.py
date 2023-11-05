from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.botany.models import Plant, Group
from django.db.models import Q


class PlantHomepageView(LoginRequiredMixin, TemplateView):
    """
    View for rendering the plant module homepage.
    """
    template_name = 'botany/homepage.html'

    def get_plants_for_group(self, default_group):
        """
        Return all plants for the currently logged-in user in the default group.
        """
        return Plant.objects.filter(user=self.request.user, group=default_group).order_by('added_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        current_group = Group.objects.get(user=self.request.user, position=1)
        user_groups = Group.objects.filter(user=self.request.user).order_by('position')
        
        current_group_index = list(user_groups).index(current_group)
        prev_group = user_groups[current_group_index - 1] if current_group_index > 0 else None
        next_group = user_groups[current_group_index + 1] if current_group_index < user_groups.count() - 1 else None

        context['current_group'] = current_group
        context['prev_group_id'] = prev_group.id if prev_group else None
        context['next_group_id'] = next_group.id if next_group else None
        context['plants'] = self.get_plants_for_group(current_group)

        return context
