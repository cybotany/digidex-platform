from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from ..models import Plant, Label


class BotanyHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'botany/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fetch labeled plant groups
        context['plant_groups'] = Label.objects.filter(user=self.request.user).prefetch_related('plants')
        # fetch unlabeled plants
        context['unlabeled_plants'] = Plant.objects.filter(owner=self.request.user, label=None)
        return context
