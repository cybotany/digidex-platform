import logging
from django.views.generic.edit import DeleteView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from digidex.journal.models import entry as base_entry

logger = logging.getLogger(__name__)

class DeleteJournalEntry(LoginRequiredMixin, DeleteView):
    model = base_entry.Entry

    def get_object(self, queryset=None):
        entry_pk = self.kwargs.get('pk')
        if not entry_pk:
            raise Http404("No Entry provided")

        entry = get_object_or_404(base_entry.Entry, id=entry_pk)
        content_object = entry.collection.content_object

        if hasattr(content_object, 'ntag') and content_object.ntag.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this entry.")

        return entry

    def delete(self, request, *args, **kwargs):
        """
        Call the superclass's delete method to perform the deletion and then
        add a success message.
        """
        obj = self.get_object()
        success_message = "Entry deleted successfully."
        response = super().delete(request, *args, **kwargs)
        messages.success(request, success_message)
        return response

    def get_success_url(self):
        collection = self.object.collection
        return reverse('journal:collection', kwargs={'pk': collection.id})
