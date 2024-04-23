from django.urls import path

from link import views

app_name = 'link'
urlpatterns = [
    path('digit/<str:serial_number>/', views.LinkDigit.as_view(), name='digit'),
]
