import logging
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.http import Http404
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.inventory.models import MODEL_MAP

logger = logging.getLogger(__name__)

class DeleteDigit(LoginRequiredMixin, DeleteView):
    def get_object(self, queryset=None):
        digit_type = self.request.GET.get('type')
        uuid = self.request.GET.get('uuid')

        if not uuid:
            raise Http404("No UUID provided")

        model = MODEL_MAP.get(digit_type)
        if not model:
            raise Http404(f"Invalid digit type '{digit_type}'")

        obj = get_object_or_404(model, uuid=uuid)
        user = self.request.user
        if obj.ntag.user != user:
            raise PermissionDenied(f"You do not have permission to delete this {model.__name__.lower()}.")

        self.model = model
        return obj

    def get_success_url(self):
        return reverse('inventory:detail-profile', kwargs={'user_slug': self.request.user.slug})

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        success_message = f"The {obj.__class__.__name__.lower()} '{obj}' was deleted successfully."
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, success_message)
        return response
