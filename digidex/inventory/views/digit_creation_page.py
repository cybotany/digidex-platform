from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from digidex.inventory.forms import DigitForm
from digidex.inventory.models import Digit, Link
from digidex.journal.models import Collection
from digidex.accounts.models import Activity


class DigitCreationView(LoginRequiredMixin, CreateView):
    model = Digit
    form_class = DigitForm
    template_name = 'main/digit-creation-page.html'

    def get_form_kwargs(self):
        kwargs = super(DigitCreationView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        # Retrieve the link instance using link_uuid from the URL
        link_uuid = self.kwargs.get('link_uuid')
        link = get_object_or_404(Link, uuid=link_uuid)

        with transaction.atomic():
            # Prepare the Digit instance but don't save it yet
            digit = form.save(commit=False)
            digit.nfc_link = link

            # Create a new Journal Collection instance
            journal_collection = Collection.objects.create()
            digit.journal_collection = journal_collection
            digit.save()

            # Update the Link object
            link.user = self.request.user
            link.active = True
            link.save()

            Activity.objects.create(
                user=self.request.user,
                activity_type='Plant',
                activity_status='Registered',
                content=f'Registered Plant {digit.name}'
            )

        return redirect('inventory:details', digit_uuid=digit.uuid)
