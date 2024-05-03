from django.urls import path

from nfc import views

urlpatterns = [
    path('<uuid:_uuid>/', views.view_ntag, name='view-ntag'),
    path('<uuid:_uuid>/link', views.link_ntag, name='link-ntag'),
]
