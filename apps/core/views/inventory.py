from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.forms import CreateGroupForm
from apps.inventory.models import Group


class InventoryView(LoginRequiredMixin, ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'inventory.html'
    paginate_by = 15

    def get_queryset(self):
        """ Overriding to get groups for the current user """
        return Group.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        """ Add form to context """
        context = super().get_context_data(**kwargs)
        context['form'] = CreateGroupForm()
        return context

    def post(self, request, *args, **kwargs):
        """ Handle the POST request - form submission """
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            new_group = form.save(commit=False)
            new_group.user = request.user
            new_group.save()
            return redirect('home')

        # Handling invalid form case
        return self.get(request, form=form)
