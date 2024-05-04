from django.urls import path

from digitization import views

urlpatterns = [
    path('<uuid:_uuid>/link/digit/', views.link_ntag_and_digit, name='link_ntag'),
    path('<int:digit_id>/link/user/', views.link_digit_and_user, name='link_user'),
    path('<int:digit_id>/link/image/', views.link_digit_and_image, name='link_image'),
]
