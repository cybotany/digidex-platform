from django.urls import path

from inventory import views

app_name = 'nfc'
urlpatterns = [
    path('<uuid:ntag_uuid>/', views.route_ntag_url, name='route_ntag'),
]
