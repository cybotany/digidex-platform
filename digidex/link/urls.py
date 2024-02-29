from django.urls import path
from digidex.link.views import NTAGLink

app_name = 'link'
urlpatterns = [
    path('digit/<str:serial_number>/', NTAGLink.as_view(), name='digit'),
]
