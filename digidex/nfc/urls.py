from django.urls import path

from nfc.views import view_ntag, link_ntag

urlpatterns = [
    path('ntag/<serial_number>/', view_ntag, name='view_ntag'),
    path('ntag/<serial_number>/link', link_ntag, name='link_ntag'),
]
