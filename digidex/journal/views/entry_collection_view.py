from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.journal.models import Entry, Collection


class EntryCollectionView(LoginRequiredMixin, ListView):
    model = Entry
    context_object_name = 'entries'
    template_name = 'journal/entry-collection-page.html'

    def get_queryset(self):
        # Retrieve the collection_id from the URL
        collection_id = self.kwargs.get('pk')
        # Filter entries by the collection_id
        return Entry.objects.filter(collection__id=collection_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        collection_id = self.kwargs.get('pk')

        # Get the collection and add it to the context
        collection = Collection.objects.get(id=collection_id)
        context['collection'] = collection

        return context

