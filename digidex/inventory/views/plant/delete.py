from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.inventory.models import Plant
import logging

logger = logging.getLogger(__name__)

class DeletePlant(LoginRequiredMixin, DeleteView):
    model = Plant

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        uuid = self.kwargs.get('uuid')
        if not uuid:
            raise Http404("No uuid provided")
        plant = get_object_or_404(queryset, uuid=uuid)

        # Permission check
        user = self.request.user
        if plant.ntag.user != user:
            raise PermissionDenied("You do not have permission to delete this plant.")

        return plant

    def get_success_url(self):
        """
        Override to redirect to the user's profile page after successful deletion.
        """
        return reverse('inventory:detail-profile', kwargs={'user_slug': self.request.user.slug})


    def delete(self, request, *args, **kwargs):
        """
        Call the superclass's delete method to perform the deletion and then
        add a success message.
        """
        obj = self.get_object()
        success_message = f"The plant '{obj}' was deleted successfully."
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, success_message)
        return response
