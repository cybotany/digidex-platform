from django.urls import path

from inventory.views import link, manage, species_name_suggestion

urlpatterns = [
    path("link/<uuid:uuid>/", link, name="link-tag"),
    path("manage/<uuid:uuid>/", manage, name="manage-tag"),
    path("species-autocomplete/", species_name_suggestion, name='species_autocomplete'),
]
