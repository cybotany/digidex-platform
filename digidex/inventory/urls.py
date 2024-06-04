from django.urls import path

from inventory import views

app_name = 'inventory'
urlpatterns = [
    path('<slug:user_slug>/link/<uuid:ntag_uuid>/', views.add_digit_view, name='add_digit'),
]
