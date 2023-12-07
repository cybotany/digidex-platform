from django.views.generic.detail import DetailView
from apps.inventory.models import Group, Digit  # Import Digit model

class GroupingView(DetailView):
    model = Group
    template_name = 'grouping.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.object
        context['digits'] = Digit.objects.filter(group=group)
        return context
