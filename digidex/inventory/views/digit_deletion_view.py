from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.inventory.models import Digit
import logging

logger = logging.getLogger(__name__)

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
        if digit.nfc_link.user != user:
            raise PermissionDenied("You do not have permission to delete this digit.")

        return digit

    def delete(self, request, *args, **kwargs):
        """
        Call the superclass's delete method to perform the deletion and then
        add a success message.
        """
        obj = self.get_object()
        success_message = f"The digit '{obj}' was deleted successfully."
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, success_message)
        return response
