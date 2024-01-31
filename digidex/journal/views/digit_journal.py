from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView
from digidex.inventory.views.base_digit_view import BaseDigitView
from digidex.journal.forms import JournalEntry
from digidex.journal.models import Entry


class DigitJournalView(BaseDigitView, CreateView):
    model = Entry
    form_class = JournalEntry
    template_name = 'journal/journal-page.html'

    def form_valid(self, form):
        # Here, self.get_object() will get the Digit instance, thanks to BaseDigitView
        digit = self.get_object()

        # Setting the digit for the journal entry
        form.instance.digit = digit

        # Save the journal entry
        return super().form_valid(form)

    def form_invalid(self, form):
        # Render the template with the invalid form.
        return render(self.request, self.template_name, {'form': form})

    def get_success_url(self):
        return reverse_lazy('inventory:digit-details', kwargs={'serial_number': self.object.digit.nfc_link.serial_number})