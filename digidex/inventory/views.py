from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from inventory.models import InventoryPage


class InventoryDetailView(DetailView):
    model = InventoryPage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InventoryListView(ListView):
    model = InventoryPage
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

