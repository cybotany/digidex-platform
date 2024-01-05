from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView
from apps.inventory.forms import CreateDigitForm
from apps.inventory.models import Digit
from apps.nfc.models import Link
from django.db import transaction


class DigitCreationView(CreateView):
    model = Digit
    form_class = CreateDigitForm
    template_name = 'inventory/digit_creation.html'

    def get_form_kwargs(self):
        kwargs = super(DigitCreationView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        # Retrieve the link instance using link_id from the URL
        link_id = self.kwargs.get('link_id')
        link = get_object_or_404(Link, id=link_id)

        with transaction.atomic():
            digit = form.save(commit=False)
            digit.nfc_link = link
            digit.save()
            
            # Update the Link objects
            link.user = self.request.user
            link.active = True
            link.save()

        return redirect('inventory:details', pk=digit.pk)