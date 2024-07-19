from django.urls import path

from gbif.views import SpeciesDetailView, SpeciesListView


urlpatterns = [
    path("<slug:slug>/", SpeciesDetailView.as_view(), name="species-detail"),
    path("", SpeciesListView.as_view(), name="species-list"),
]
