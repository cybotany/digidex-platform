from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from digidex.journal.models import entry as base_entry

class DetailJournalEntry(LoginRequiredMixin, DetailView):
    model = base_entry.Entry
    template_name = 'journal/entry/detail-page.html'
    context_object_name = 'entry'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        entry = get_object_or_404(base_entry.Entry, pk=pk)        
        entity = entry.collection.content_object
        if hasattr(entity, 'ntag') and entity.ntag.user != self.request.user:
            raise PermissionDenied("You do not have permission to view this entry.")
        
        return entry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entry = context.get('entry')

        collection_url = entry.collection.get_absolute_url()
        entity_url = entry.collection.get_entity_url()
        
        entry_heading = f"{entry.collection.get_entity_name()}'s Journal"
        entry_date = entry.created_at.strftime('%B %d, %Y')
        entry_number = f"Entry {entry.entry_number}"

        context.update({
            'subtitle': 'Entry',
            'heading': entry_heading,
            'date': entry_date,
            'paragraph': entry_number,
            'collection_url': collection_url,
            'entity_url': entity_url,
        })
        return context
