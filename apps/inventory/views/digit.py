from django.views.generic import DetailView
from django.shortcuts import redirect, render
from apps.inventory.models import Digit
from apps.inventory.forms import DigitizationForm


class DigitView(DetailView):
    model = Digit
    template_name = 'inventory/digit.html'

    def link_is_active(self):
        """Check if the associated Link is active."""
        return self.object.nfc_link.active if self.object.nfc_link else False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_active'] = self.link_is_active()
        context['digitization_form'] = DigitizationForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = DigitizationForm(request.POST, request.FILES, instance=self.object)
        if form.is_valid():
            form.save()
            return redirect(self.object.get_absolute_url())

        context = self.get_context_data(object=self.object)
        context['digitization_form'] = form
        return render(request, self.template_name, context)
