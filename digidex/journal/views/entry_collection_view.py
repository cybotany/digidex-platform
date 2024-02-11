from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.journal.models import Entry, Collection

class EntryCollectionView(LoginRequiredMixin, ListView):
    model = Entry
    context_object_name = 'entries'
    template_name = 'journal/entry-collection-page.html'

    def get_queryset(self):
        # Retrieve the collection_id from the URL
        collection_id = self.kwargs.get('pk')

        # Ensure the collection exists and is associated with the current user
        collection = Collection.objects.filter(id=collection_id).select_related('digit__nfc_link').first()
        if not collection or collection.digit.nfc_link.user != self.request.user:
            raise PermissionDenied("You do not have permission to view these entries.")

        # Use select_related to optimize the query
        return Entry.objects.filter(collection=collection).select_related('collection__digit')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        collection_id = self.kwargs.get('pk')
        collection = Collection.objects.get(id=collection_id)

        collection_heading = f"{collection.get_digit_name()}'s Journal"
        collection_paragraph = collection.get_digit_description()
        digit_url = collection.get_digit_url()

        context.update({
            'subtitle': 'Collection',
            'heading': collection_heading,
            'paragraph': collection_paragraph,
            'digit_url': digit_url,
        })
        return context
