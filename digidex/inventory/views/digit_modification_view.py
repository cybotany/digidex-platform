from django.views.generic.edit import UpdateView
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
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
        digit = get_object_or_404(queryset, uuid=uuid)

        # Permission check
        user = self.request.user
        if digit.nfc_tag.user != user:
            raise PermissionDenied("You do not have permission to view this digit.")

        return digit

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

    def get_success_url(self):
        """
        After successfully updating the digit, redirect to the digit's URL.
        """
        return self.object.get_absolute_url()