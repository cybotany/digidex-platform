from django.urls import path

from inventory.views import link_ntag, delete_digit

urlpatterns = [
    path('ntag/<uuid:ntag_uuid>/link', link_ntag, name='link_ntag'),
    path('digit/<uuid:digit_uuid>/deletion', delete_digit, name='delete_digit'),
]
