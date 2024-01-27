from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from digidex.inventory.forms import DigitForm
from digidex.inventory.models import Digit


class DigitModificationView(LoginRequiredMixin, UpdateView):
    model = Digit
    form_class = DigitForm
    template_name = 'main/digit-modification-page.html'

    def get_object(self, queryset=None):
        uuid = self.kwargs.get('uuid')
        obj = get_object_or_404(Digit, uuid=uuid)

        if obj.nfc_link.user != self.request.user:
            raise PermissionDenied
        return obj

    def form_valid(self, form):
        with transaction.atomic():
            # Save the Digit instance
            self.object = form.save()
        return redirect('inventory:details', uuid=self.object.uuid)
