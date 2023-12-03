from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.models import Group


class DisplayGroupView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'display_group.html'
    context_object_name = 'groups'
    paginate_by = 1

    def get_queryset(self):
        """
        Return the list of Groups for the current user.
        """
        return Group.objects.filter(user=self.request.user).prefetch_related('digits_set')
