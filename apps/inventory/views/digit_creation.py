from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.db import transaction
from apps.inventory.forms import DigitForm
from apps.inventory.models import Digit
from apps.nfc.models import Link
from apps.accounts.models import Activity


class DigitCreationView(CreateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit_creation.html'

    def get_form_kwargs(self):
        kwargs = super(DigitCreationView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        # Retrieve the link instance using link_id from the URL
        link_pk = self.kwargs.get('pk')
        link = get_object_or_404(Link, pk=link_pk)

        with transaction.atomic():
            digit = form.save(commit=False)
            digit.nfc_link = link
            digit.save()
            
            # Update the Link objects
            link.user = self.request.user
            link.active = True
            link.save()

            Activity.objects.create(
                user=self.request.user,
                activity_type='Plant',
                activity_status='Registered',
                content=f'Registered Plant {digit.name}'
            )

        return redirect('inventory:details', pk=digit.pk)