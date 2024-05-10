from django.urls import path

from inventory import views

app_name = 'inventory'
urlpatterns = [
    path('link/ntag/<uuid:ntag_uuid>/', views.link_ntag_and_digit, name='link_ntag'),
    path('add/digit/<uuid:digit_uuid>/note/', views.add_digit_note, name='add_digit_note'),
]