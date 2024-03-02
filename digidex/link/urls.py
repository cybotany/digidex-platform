from django.urls import path

from digidex.link.views.nfc.tag import base as ntag

app_name = 'link'
urlpatterns = [
    path('digit/<str:serial_number>/', ntag.LinkDigit.as_view(), name='digit'),
]
