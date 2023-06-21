from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.botany.models import Label


class PlantHomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'botany/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plant_groups = Label.objects.filter(user=self.request.user, plant__isnull=False).distinct().prefetch_related('plant_set')
        context['plant_groups'] = list(plant_groups)
        return context
