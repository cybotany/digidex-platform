from django.urls import path

from nfc import views

urlpatterns = [
    path('<uuid:_uuid>/', views.route_ntag_url, name='route_ntag'),
]