from django.urls import path

from inventory.views import link, manage

urlpatterns = [
    path("link/<uuid:uuid>/", link, name="link-tag"),
    path("manage/<uuid:uuid>/", manage, name="manage-tag"),
]
