from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from digidex.utils.helpers import BaseDigitView
from digidex.inventory.models import Digit


class DigitDeletionView(BaseDigitView, DeleteView):
    model = Digit    
    success_url = reverse_lazy('inventory:storage')

    def get_object(self, queryset=None):
        # Use the BaseDigitView's get_object method to get the associated Digit
        return super().get_object(queryset=queryset)
