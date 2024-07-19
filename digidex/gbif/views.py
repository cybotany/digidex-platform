from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from gbif.models import GBIFSpecies


class SpeciesDetailView(DetailView):
    model = GBIFSpecies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SpeciesListView(ListView):
    model = GBIFSpecies
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
