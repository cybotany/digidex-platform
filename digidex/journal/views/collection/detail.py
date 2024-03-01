from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from digidex.journal.models import entry as base_entry
from digidex.journal.models import collection as base_collection

class DetailJournalCollection(LoginRequiredMixin, ListView):
    model = base_entry.Entry
    context_object_name = 'entries'
    template_name = 'journal/entry-collection-page.html'

    def get_queryset(self):
        collection_id = self.kwargs.get('pk')
        collection = get_object_or_404(base_collection.Collection, id=collection_id)

        if collection.content_object and getattr(collection.content_object, 'ntag', None) and collection.content_object.ntag.user != self.request.user:
            raise PermissionDenied("You do not have permission to view these entries.")

        return base_entry.Entry.objects.filter(collection=collection)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        collection_id = self.kwargs.get('pk')
        collection = base_collection.Collection.objects.get(id=collection_id)

        collection_heading = f"{collection.get_entity_name()}'s Journal"
        collection_paragraph = collection.get_entity_description()
        entity_url = collection.get_entity_url()

        context.update({
            'subtitle': 'Collection',
            'heading': collection_heading,
            'paragraph': collection_paragraph,
            'entity_url': entity_url,
        })
        return context
