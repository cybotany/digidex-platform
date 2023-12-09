from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.models import Link


class GroupedLinksView(LoginRequiredMixin, ListView):
    model = Link
    context_object_name = 'links'
    template_name = 'grouped_links.html'

    def get_queryset(self):
        """ Overriding to get links for the current group """
        group_id = self.kwargs.get('group_id')
        return Link.objects.filter(group_id=group_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
