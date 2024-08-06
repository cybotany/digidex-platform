from django.urls import path

from inventory.views import link, manage, species_autocomplete

urlpatterns = [
    path("link/<uuid:uuid>/", link, name="link-tag"),
    path("manage/<uuid:uuid>/", manage, name="manage-tag"),
    path("species-autocomplete/", species_autocomplete, name='species_autocomplete'),
]
