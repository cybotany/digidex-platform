from django.urls import path
from digidex.link.views import NFCLinkView

app_name = 'link'
urlpatterns = [
    path('digit/<slug:slug>/', NFCLinkView.as_view(), name='digit-link'),
]
