from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from digidex.journal.models import Entry

class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'journal/entry-details-page.html'
    context_object_name = 'entry'

    def get_object(self, queryset=None):
        # Retrieve the entry based on the passed UUID or primary key
        pk = self.kwargs.get('pk')
        entry = get_object_or_404(Entry, pk=pk)

        # Check if the logged-in user owns the digit linked to the entry's collection
        if entry.collection.digit.nfc_link.user != self.request.user:
            raise PermissionDenied("You do not have permission to view this entry.")
        
        return entry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entry = context.get('entry')

        collection_url = entry.collection.get_absolute_url() if entry.collection else "#"
        digit_url = entry.collection.digit.get_absolute_url() if entry.collection and entry.collection.digit else "#"
        
        entry_heading = f"{entry.collection.get_digit_name()}'s Journal"
        entry_date = entry.created_at.strftime('%B %d, %Y')
        entry_number = f"Entry {entry.get_entry_number()}"

        context.update({
            'subtitle': 'Entry',
            'heading': entry_heading,
            'date': entry_date,
            'paragraph': entry_number,
            'digit_url': digit_url,
            'collection_url': collection_url,
        })
        return context
