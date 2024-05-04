from django.urls import path

from digitization import views

app_name = 'digitization'
urlpatterns = [
    path('<uuid:ntag_uuid>/link/ntag/', views.link_ntag_and_digit, name='link_ntag'),
    path('<uuid:digit_uuid>/link/user/', views.link_digit_and_user, name='link_user'),
    path('<uuid:digit_uuid>/link/image/', views.link_digit_and_image, name='link_image'),
]
