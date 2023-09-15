from django.urls import path
from apps.nfc.views import HandleNFCView

app_name = 'nfc'
urlpatterns = [
    path('register/<str:nfc_sn>/', HandleNFCView.as_view(), name='tag-registration'),
]
