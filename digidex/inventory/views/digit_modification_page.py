from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from digidex.inventory.forms import DigitForm
from digidex.inventory.models import Digit
from digidex.accounts.models import Activity


class DigitModificationView(LoginRequiredMixin, UpdateView):
    model = Digit
    form_class = DigitForm
    template_name = 'main/digit-modification-page.html'

    def get_object(self, queryset=None):
        digit_uuid = self.kwargs.get('digit_uuid')
        obj = get_object_or_404(Digit, uuid=digit_uuid)

        if obj.nfc_link.user != self.request.user:
            raise PermissionDenied
        return obj

    def form_valid(self, form):
        with transaction.atomic():
            # Save the Digit instance
            self.object = form.save()

            Activity.objects.create(
                user=self.request.user,
                activity_type='Plant',
                activity_status='Updated',
                content=f'Updated Plant {self.object.name}'
            )

        return redirect('inventory:details', digit_uuid=self.object.uuid)
