from django.urls import path

from digidex.link.views.nfc import base 

app_name = 'link'
urlpatterns = [
    path('digit/<str:serial_number>/', base.LinkDigitAndNtag.as_view(), name='digit'),
]
