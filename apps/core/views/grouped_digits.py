from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.models import Link
from apps.core.models import Digit


class GroupedDigitsView(LoginRequiredMixin, ListView):
    context_object_name = 'digits'
    template_name = 'grouped_digits.html'

    def get_queryset(self):
        """ Overriding to get Digits mapped to each active link in the current group """
        group_id = self.kwargs.get('group_id')
        # Get the primary keys of Digits from active links in the group
        digit_pks = Link.objects.filter(group_id=group_id, active=True).values_list('digit', flat=True)
        # Retrieve and return the associated Digit instances
        return Digit.objects.filter(pk__in=digit_pks)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
