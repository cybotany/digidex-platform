from django.urls import path

from inventory.views import link, species_name_suggestion, species_name_lookup

urlpatterns = [
    path("link/<uuid:uuid>/", link, name="link-tag"),
    path("ajax/species-autocomplete/", species_name_suggestion, name='species_autocomplete'),
    path("ajax/species-lookup/", species_name_lookup, name='species_lookup'),
]
