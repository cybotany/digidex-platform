from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.journal.models import Entry, Collection
from digidex.journal.forms import JournalEntry


class EntryCreationView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = JournalEntry
    template_name = 'journal/entry-creation-page.html'

    def dispatch(self, request, *args, **kwargs):
        collection_id = self.kwargs.get('pk')
        collection = get_object_or_404(Collection, pk=collection_id)
        if collection.digit.nfc_link.user != self.request.user:
            raise PermissionDenied("You do not have permission to add an entry to this collection.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        collection_id = self.kwargs.get('pk')
        form.instance.collection = get_object_or_404(Collection, pk=collection_id)
        return super().form_valid(form)
