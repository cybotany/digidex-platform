from django.views.generic import DetailView
from digidex.utils.helpers import BaseDigitView
from digidex.inventory.models import Digit
from digidex.journal.forms import JournalEntry


class DigitDetailView(BaseDigitView, DetailView):
    model = Digit
    template_name = 'inventory/digit-details-page.html'

    def get_object(self, queryset=None):
        # Use the BaseDigitView's get_object method to get the associated Digit
        return super().get_object(queryset=queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        digit = self.object

        # Access the related Journal Collection and its entries
        journal_entries = digit.journal_collection.entries.all()
        context['journal_entries'] = journal_entries[:10]

        # Include journal entry form in the context
        context['journal_entry_form'] = JournalEntry()


        context['collection_id'] = digit.journal_collection.id

        # Optionally, if you have images associated with journal entries and want the latest image
        last_image_entry = journal_entries.filter(image__isnull=False).order_by('-created_at').first()
        context['last_image'] = last_image_entry.image if last_image_entry else None

        return context
