from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.journal.models import Collection


class JournalStorageView(LoginRequiredMixin, ListView):
    model = Collection
    context_object_name = 'collections'
    template_name = 'inventory/digit-storage-page.html'

    #def get_queryset(self):
    #    """ Overriding to get Digits for the current user """
    #    return Collection.objects.filter(nfc_link__user=self.request.user)
    #        context.update({
    #        'subtitle': '',
    #        'heading': '',
    #        'paragraph': ''
    #    })
