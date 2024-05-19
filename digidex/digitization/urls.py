from django.urls import path

from digitization.views import link_ntag_and_digit

app_name = 'digitization'
urlpatterns = [
    path('<slug:profile_slug>/link/ntag/<uuid:ntag_uuid>/', link_ntag_and_digit, name='link_ntag'),
]
