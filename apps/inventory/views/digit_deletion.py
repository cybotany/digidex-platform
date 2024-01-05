from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.models import Digit
from django.db import transaction


class DigitDeletionView(LoginRequiredMixin, View):
    def post(self, request, pk):
        with transaction.atomic():
            digit = get_object_or_404(Digit, pk=pk)

            if digit.nfc_link:
                link = digit.nfc_link
                link.reset_to_default()
                digit.delete()

        return redirect('inventory:storage')
