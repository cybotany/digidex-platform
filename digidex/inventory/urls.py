from django.urls import path

from inventory.views import link

urlpatterns = [
    path("<uuid:uuid>/", link, name="link-tag"),
]
