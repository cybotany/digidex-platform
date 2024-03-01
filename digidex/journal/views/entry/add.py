import logging
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from digidex.journal.forms import entry as entry_form
from digidex.journal.models import entry as base_entry
from digidex.journal.models import collection as base_collection

logger = logging.getLogger(__name__)

class AddJournalEntry(LoginRequiredMixin, CreateView):
    model = base_entry.Entry
    form_class = entry_form.JournalEntryForm
    template_name = 'journal/entry/form-page.html'

    def dispatch(self, request, *args, **kwargs):
        collection_id = self.kwargs.get('pk')
        collection = get_object_or_404(base_collection.Collection, pk=collection_id)
        content_object = collection.content_object

        if hasattr(content_object, 'ntag') and content_object.ntag.user != request.user:
            raise PermissionDenied("You do not have permission to add an entry to this collection.")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        collection_id = self.kwargs.get('pk')
        form.instance.collection = get_object_or_404(base_collection.Collection, pk=collection_id)
        messages.success(self.request, "Entry added successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was a problem with the form. Please check the details you entered.")
        return super().form_invalid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()
