from django.views.generic.edit import UpdateView
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.inventory.models import Digit
from digidex.inventory.forms import DigitForm


class DigitModificationView(LoginRequiredMixin, UpdateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit-modification-page.html'

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        uuid = self.kwargs.get('uuid')
        if not uuid:
            raise Http404("No uuid provided")
        return get_object_or_404(queryset, uuid=uuid)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

    def get_success_url(self):
        """
        After successfully updating the digit, redirect to the digit's URL.
        """
        return self.object.get_absolute_url()