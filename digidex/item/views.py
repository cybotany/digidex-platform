from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from item.models import Item


class ItemDetailView(DetailView):
    context_object_name = "item"
    template_name = "item/item_detail.html"

    def get_queryset(self):
        return get_object_or_404(Item, slug=self.kwargs["inventory_slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
