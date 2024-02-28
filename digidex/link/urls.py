from django.urls import path
from digidex.link.views import NTAGLink

app_name = 'link'
urlpatterns = [
    path('digit/<slug:slug>/', NTAGLink.as_view(), name='digit'),
]
