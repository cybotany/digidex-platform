from django.urls import path
from digidex.link.views import NFCLinkView

app_name = 'link'
urlpatterns = [
    path('digit/<str:serial_number>/', NFCLinkView.as_view(), name='digit'),
]
