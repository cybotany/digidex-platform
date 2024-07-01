from django.urls import path

from nfc import views

app_name = 'nfc'
urlpatterns = [
    path('<uuid:nfc_uuid>/', views.route_nfc_tag_url, name='route_nfc_tag'),
    path('<uuid:nfc_uuid>/mapping/', views.map_nfc_tag, name='map_nfc_tag'),
]
