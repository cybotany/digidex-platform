from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.journal.models import Entry, Collection
from digidex.journal.forms import JournalEntry


class EntryCreationView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = JournalEntry
    template_name = 'journal/entry-creation-page.html'

    def form_valid(self, form):
        collection_id = self.kwargs.get('pk')
        collection = get_object_or_404(Collection, pk=collection_id)
        form.instance.collection = collection
        return super().form_valid(form)
