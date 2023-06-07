from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from ..models import Label

class BotanyHomeView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'botany/home.html'
    context_object_name = 'plant_groups'

    def get_queryset(self):
        return Label.objects.filter(user=self.request.user).prefetch_related('plants')
