from django.views.generic.detail import DetailView
from apps.inventory.models import Group
from apps.inventory.models import Link

class GroupingView(DetailView):
    model = Group
    template_name = 'grouping.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.object
        context['links'] = Link.objects.filter(group=group)
        return context
