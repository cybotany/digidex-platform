from django.urls import path

from digitization.views import link_ntag, delete_digit

app_name = 'digitization'
urlpatterns = [
    path('ntag/<uuid:ntag_uuid>/', link_ntag, name='link_ntag'),
    path('<uuid:digit_uuid>/deletion', delete_digit, name='delete_digit'),
]
