from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib import messages
from digidex.inventory.models import Grouping
from digidex.inventory.forms import GroupingForm


class CreateGrouping(LoginRequiredMixin, CreateView):
    model = Grouping
    form_class = GroupingForm
    template_name = 'inventory/grouping/form-page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Group added successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "There was a problem with the form. Please check the details you entered.")
        return super().form_invalid(form)
