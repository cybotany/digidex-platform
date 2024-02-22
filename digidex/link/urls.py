from django.urls import path
from digidex.link.views import NTAGLinkView

app_name = 'link'
urlpatterns = [
    path('digit/<str:serial_number>/', NTAGLinkView.as_view(), name='digit'),
]
