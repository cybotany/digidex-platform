from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from digidex.link.views import BaseNFCLinkedView
from digidex.inventory.models import Digit


class DigitDeletionView(BaseNFCLinkedView):
    success_url = reverse_lazy('inventory:storage')
