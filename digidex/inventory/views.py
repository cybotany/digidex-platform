from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from inventory.models import InventoryPage


class InventoryDashboardView(DetailView):
    context_object_name = "inventory"
    template_name = "inventory/dashboard.html"

    def get_queryset(self):
        return get_object_or_404(InventoryPage, slug=self.kwargs["inventory_slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
