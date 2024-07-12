from django.urls import path, include

from nearfieldcommunication.api import router
from nearfieldcommunication.views import route_nfc_link

urlpatterns = [
    path("api/", include(router.urls)),
    path("nfc/<uuid:nfc_uuid>/", route_nfc_link, name="route_nfc_link"),
]

