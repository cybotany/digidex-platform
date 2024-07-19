from django.views.generic.detail import DetailView

from category.models import CategoryPage


class CategoryDetailView(DetailView):
    context_object_name = "category"
    model = CategoryPage
    template_name = "category/category_detail.html"

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
