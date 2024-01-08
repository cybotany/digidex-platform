from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import UpdateView
from django.db import transaction
from apps.inventory.forms import DigitForm
from apps.inventory.models import Digit
from apps.accounts.models import Activity


class DigitModificationView(UpdateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit_modification.html'

    def get_object(self, queryset=None):
        digit_id = self.kwargs.get('pk')
        return get_object_or_404(Digit, pk=digit_id)

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

        return redirect('inventory:details', pk=self.object.pk)
