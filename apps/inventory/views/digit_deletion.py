from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.models import Digit
from apps.nfc.models import Link
from django.db import transaction


class DigitDeletionView(LoginRequiredMixin, View):
    def post(self, request, pk):
        with transaction.atomic():
            # Get the Digit and associated Link
            digit = get_object_or_404(Digit, pk=pk)
            link = get_object_or_404(Link, digit=digit)

            # Delete the old Digit
            digit.delete()

            # Set Link to inactive
            link.active = False
            link.save()

            # Create a new Digit and associate it with the Link
            new_digit = Digit.objects.create(nfc_link=link)
        return redirect('inventory:storage')
