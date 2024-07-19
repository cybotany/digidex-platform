from django.views.generic.detail import DetailView

from item.models import ItemPage


class ItemDetailView(DetailView):
    context_object_name = "item"
    model = ItemPage
    template_name = "item/item_detail.html"

    def get_panels(self):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_panels()
        return context
