from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from inventory.models import Inventory, Category, Item


class CategoryDetailView(DetailView):
    context_object_name = "category"
    template_name = "category/category_detail.html"

    def get_queryset(self):
        return get_object_or_404(Category, slug=self.kwargs["inventory_slug"])

    def get_collection(self, items=None):
        from base.components import CollectionComponent, EmptyComponent
        if items:
            return CollectionComponent(
            children=[item.get_component() for item in items],
            style="post",
        )
        else:
            return EmptyComponent(asset="items")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collection"] = self.get_collection()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ItemDetailView(DetailView):
    context_object_name = "item"
    template_name = "item/item_detail.html"

    def get_queryset(self):
        return get_object_or_404(Item, slug=self.kwargs["inventory_slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
