from django.db import transaction
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.models import Digit
from apps.accounts.models import Activity


class DigitDeletionView(LoginRequiredMixin, View):
    def post(self, request, pk):
        with transaction.atomic():
            digit = get_object_or_404(Digit, pk=pk)

            if digit.nfc_link:
                link = digit.nfc_link
                link.reset_to_default()

                Activity.objects.create(
                    user=request.user,
                    activity_type='Plant',
                    activity_status='Deleted',
                    content=f'Deleted Plant {digit.name}'
                )

                digit.delete()

        return redirect('inventory:storage')
