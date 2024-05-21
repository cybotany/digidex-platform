from django.urls import path

from digitization import views

app_name = 'digitization'
urlpatterns = [
    path('link-ntag/<uuid:ntag_uuid>/', views.create_digit_with_ntag, name='link_ntag'),
]
