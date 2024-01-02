from django.views import View
from django.shortcuts import get_object_or_404, redirect
from apps.inventory.models import Digit
from apps.nfc.models import Link
from django.db import transaction


class DeleteDigitView(View):
    def post(self, request, pk):
        with transaction.atomic():
            digit = get_object_or_404(Digit, pk=pk)

            link = get_object_or_404(Link, digit=digit)
            link.active = False
            link.save()

            digit.delete()
        return redirect('inventory:garden')
