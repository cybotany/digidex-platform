from django.views.generic.edit import UpdateView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.inventory.models import Pet
from digidex.inventory.forms import PetForm
import logging

logger = logging.getLogger(__name__)

class PetModification(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'inventory/pet/modification-page.html'

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        uuid = self.kwargs.get('uuid')
        if not uuid:
            raise Http404("No uuid provided")
        pet = get_object_or_404(queryset, uuid=uuid)

        # Permission check
        user = self.request.user
        if pet.ntag.user != user:
            raise PermissionDenied("You do not have permission to view this pet.")

        return pet

    def form_valid(self, form):
        """
        If the form is valid, save the updated pet and send a success message.
        """
        response = super().form_valid(form)
        messages.success(self.request, "Pet updated successfully.")
        return response

    def form_invalid(self, form):
        """
        If the form is invalid, optionally add an error message before re-rendering the form.
        """
        messages.error(self.request, "There was a problem with the form. Please check the details you entered.")  # Optionally add error message
        return super().form_invalid(form)

    def get_success_url(self):
        """
        After successfully updating the pet, redirect to the pet's URL.
        """
        return self.object.get_absolute_url()
