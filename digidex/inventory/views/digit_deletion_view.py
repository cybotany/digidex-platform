from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.inventory.models import Digit


class DigitDeletionView(LoginRequiredMixin, DeleteView):
    model = Digit    
    success_url = reverse_lazy('inventory:digit-storage')

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        uuid = self.kwargs.get('uuid')
        if not uuid:
            raise Http404("No uuid provided")
        digit = get_object_or_404(queryset, uuid=uuid)

       # Permission check
        user = self.request.user
        if digit.nfc_tag.user != user:
            raise PermissionDenied("You do not have permission to view this digit.")

        return digit
