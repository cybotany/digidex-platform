from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from digidex.inventory.models import Digit


class DigitDeletionView(LoginRequiredMixin, DeleteView):
    model = Digit
    success_url = reverse_lazy('inventory:storage')

    def get_object(self, queryset=None):
        serial_number = self.kwargs.get('serial_number')
        return get_object_or_404(Digit, nfc_link__serial_number=serial_number)
