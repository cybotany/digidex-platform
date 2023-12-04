from django.views.generic.detail import DetailView
from apps.inventory.models import Group


class GroupingView(DetailView):
    model = Group
    template_name = 'grouping.html'

    def get_queryset(self):
        # Filter to ensure users can only see their own groups
        return Group.objects.filter(user=self.request.user)
