from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from category.models import CategoryPage


class CategoryDetailView(DetailView):
    model = CategoryPage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryListView(ListView):
    model = CategoryPage
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

