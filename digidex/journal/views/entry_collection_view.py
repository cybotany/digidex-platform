from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.journal.models import Entry, Collection


class EntryCollectionView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'journal/entry-collection-page.html'

    def get_queryset(self):
        # Retrieve the collection_id from the URL
        collection_id = self.kwargs.get('collection_id')
        # Filter entries by the collection_id
        return Entry.objects.filter(collection__id=collection_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        collection_id = self.kwargs.get('collection_id')
        entries = self.get_queryset()

        if entries:
            context['latest_entry'] = entries.first()
            context['other_entries'] = entries[1:]
        else:
            context['latest_entry'] = None
            context['other_entries'] = []

        collection = Collection.objects.get(id=collection_id)
        context['collection'] = collection
        return context
