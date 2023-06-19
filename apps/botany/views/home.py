from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from ..models import Plant, Label


class BotanyHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'botany/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fetch labeled plant groups
        plant_groups = Label.objects.filter(user=self.request.user).prefetch_related('plants')
        
        # fetch unlabeled plants
        unlabeled_plants = Plant.objects.filter(owner=self.request.user, label=None)
        
        # create an unlabeled group
        unlabeled_group = Label(name='', user=self.request.user)
        unlabeled_group.plants = unlabeled_plants

        # combine labeled groups and unlabeled group
        context['plant_groups'] = list(plant_groups) + [unlabeled_group]
        return context

