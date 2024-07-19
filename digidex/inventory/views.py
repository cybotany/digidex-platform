from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from inventory.models import InventoryPage


class InventoryDetailView(DetailView):
    context_object_name = "inventory"
    template_name = "inventory/inventory_detail.html"

    def get_queryset(self):
        return get_object_or_404(InventoryPage, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
