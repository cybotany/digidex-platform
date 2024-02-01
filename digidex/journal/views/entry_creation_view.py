from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView
from digidex.journal.models import Entry, Collection
from digidex.journal.forms import JournalEntry


class EntryCreationView(CreateView):
    model = Entry
    form_class = JournalEntry
    template_name = 'journal/entry-creation-page.html'

    def form_valid(self, form):
        collection_id = self.kwargs.get('collection_id')
        collection = get_object_or_404(Collection, pk=collection_id)
        form.instance.collection = collection
        return super().form_valid(form)
