from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from item.models import ItemPage


class ItemDetailView(DetailView):
    model = ItemPage

    def get_panels(self):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_panels()
        return context


class ItemListView(ListView):
    model = ItemPage
    paginate_by = 50

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
