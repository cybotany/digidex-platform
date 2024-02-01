from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from digidex.inventory.models import Digit


class DigitDeletionView(LoginRequiredMixin, DeleteView):
    model = Digit    
    success_url = reverse_lazy('inventory:digit-storage')

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        uuid = self.kwargs.get('uuid')
        if not uuid:
            raise Http404("No uuid provided")
        return get_object_or_404(queryset, uuid=uuid)
