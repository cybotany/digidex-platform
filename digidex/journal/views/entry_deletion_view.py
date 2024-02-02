from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from digidex.journal.models import Entry


class EntryDeletionView(LoginRequiredMixin, DeleteView):
    model = Entry    

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        entry_pk = self.kwargs.get('pk')
        if not entry_pk:
            raise Http404("No Entry provided")
        return get_object_or_404(queryset, id=entry_pk)

    def get_success_url(self):
            # Assuming the ForeignKey relation to Collection is named 'collection'
            collection = self.object.collection
            return reverse('journal:collection-details', kwargs={'pk': collection.id})