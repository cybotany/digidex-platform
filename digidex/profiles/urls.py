from django.urls import path

from profiles import views
from inventory.views import link_ntag_and_digit# , add_digit_note

app_name = 'profiles'
urlpatterns = [
    path('<slug:profile_slug>/update/', views.profile_form_view, name='profile_form'),
    path('<slug:profile_slug>/link/ntag/<uuid:ntag_uuid>/', link_ntag_and_digit, name='link_ntag'),
    # path('<slug:profile_slug>/add/digit/<uuid:digit_uuid>/note/', add_digit_note, name='add_digit_note'),
]
