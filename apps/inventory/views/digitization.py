from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from apps.inventory.models import Digit, Journal
from apps.inventory.forms import DigitizationForm
from apps.nfc.models import Link


class DigitizationView(CreateView):
    model = Digit
    form_class = DigitizationForm
    template_name = 'inventory/digitization.html'

    def get_form_kwargs(self):
        kwargs = super(DigitizationView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        # Retrieve the link instance using link_id from the URL
        link_id = self.kwargs.get('link_id')
        link = get_object_or_404(Link, id=link_id)

        # Set the digit instance to the form's instance and save
        digit = form.save(commit=False)
        digit.save()

        # Create an initial journal entry for the digitization
        initial_journal_entry = Journal.objects.create(
            digit=digit,
            user=self.request.user,
            entry="Initial journal entry for " + digit.name
        )

        link.active = True
        link.save()

        return super(DigitizationView, self).form_valid(form)
