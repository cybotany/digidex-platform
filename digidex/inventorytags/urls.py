from django.urls import path

from inventorytags.views import link


urlpatterns = [
    path("<uuid:uuid>/", link, name="link"),
]
