from django.urls import path

from digitization.views import link_ntag

app_name = 'digitization'
urlpatterns = [
    path('ntag/<uuid:ntag_uuid>/', link_ntag, name='link_ntag'),
]
