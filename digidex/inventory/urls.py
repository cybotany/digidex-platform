from django.urls import path

from inventory.views import link_ntag_and_digit# , add_digit_note

app_name = 'inventory'
urlpatterns = [
    path('<slug:profile_slug>/link/ntag/<uuid:ntag_uuid>/', link_ntag_and_digit, name='link_ntag'),
    # path('<slug:profile_slug>/add/digit/<uuid:digit_uuid>/note/', add_digit_note, name='add_digit_note'),
]
