from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from digidex.inventory.models import Digit
from digidex.accounts.models import Activity


class DigitDeletionView(LoginRequiredMixin, DeleteView):
    model = Digit
    success_url = reverse_lazy('inventory:storage')

    def get_object(self, queryset=None):
        digit_uuid = self.kwargs.get('digit_uuid')
        return get_object_or_404(Digit, uuid=digit_uuid)

    def delete(self, request, *args, **kwargs):
        # Start a transaction
        with transaction.atomic():
            digit = self.get_object()

            if digit.nfc_link:
                link = digit.nfc_link
                link.reset_to_default()

            Activity.objects.create(
                user=request.user,
                activity_type='Plant',
                activity_status='Deleted',
                content=f'Deleted Plant {digit.name}'
            )

            response = super(DigitDeletionView, self).delete(request, *args, **kwargs)

        return response
