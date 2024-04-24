from django.urls import path

from digidex.nfc import views

app_name = 'link'
urlpatterns = [
    path('digit/<str:serial_number>/', views.LinkDigit.as_view(), name='digit'),
]
