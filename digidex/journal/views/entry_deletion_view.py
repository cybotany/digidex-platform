from django.views.generic.edit import DeleteView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.journal.models import Entry

class EntryDeletionView(LoginRequiredMixin, DeleteView):
    model = Entry    

    def get_object(self, queryset=None):
        # Retrieve the entry based on the passed primary key
        entry_pk = self.kwargs.get('pk')
        if not entry_pk:
            raise Http404("No Entry provided")

        entry = get_object_or_404(Entry, id=entry_pk)

        # Check if the logged-in user owns the digit linked to the entry's collection
        if entry.collection.digit.nfc_link.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this entry.")

        return entry

    def get_success_url(self):
        collection = self.object.collection
        return reverse('journal:collection-details', kwargs={'pk': collection.id})
