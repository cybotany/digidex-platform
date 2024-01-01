from django.urls import path
from .views import (LinkingView, DigitizationView, DigitView, GardenView, DeleteDigitView)

app_name = 'inventory'
urlpatterns = [
    path('garden/', GardenView.as_view(), name='garden'),
    path('link/<str:serial_number>/', LinkingView.as_view(), name='linking'),
    path('digitize/<int:link_id>/', DigitizationView.as_view(), name='digitization'),
    path('digit/<int:pk>/', DigitView.as_view(), name='digit'),
    path('digit/delete/<int:pk>/', DeleteDigitView.as_view(), name='delete-digit'),
]
