from django.views.generic.detail import DetailView
from apps.inventory.models import Group
from apps.core.models import Digit

class GroupingView(DetailView):
    model = Group
    template_name = 'grouping.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.object
        context['digits'] = Digit.objects.filter(group=group)
        return context
