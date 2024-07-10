from django.urls import path
from nearfieldcommunication import views

urlpatterns = [
    path("<uuid:nfc_uuid>/", views.route_nfc_link, name="route_nfc_link"),
]
