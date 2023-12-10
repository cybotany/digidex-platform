from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.forms import CreateGroupForm
from apps.inventory.models import Link, Group
from apps.core.models import Digit


class GardenView(LoginRequiredMixin, ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'garden.html'

    def get_queryset(self):
        """ Overriding to get groups for the current user """
        return Group.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        """ Add form to context """
        context = super().get_context_data(**kwargs)
        context['form'] = CreateGroupForm()
        digit_pks = Link.objects.filter(group__isnull=True, active=True).values_list('digit', flat=True)
        context['ungrouped_digits'] = Digit.objects.filter(pk__in=digit_pks)
        return context

    def post(self, request, *args, **kwargs):
        """ Handle the POST request - form submission """
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            new_group = form.save(commit=False)
            new_group.user = request.user
            new_group.save()
            return redirect('core:garden')

        # Handling invalid form case
        return self.get(request, form=form)
