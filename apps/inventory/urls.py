from django.urls import path
from .views import (GardenView, DigitView, DeleteDigitView)

app_name = 'inventory'
urlpatterns = [
    path('garden/', GardenView.as_view(), name='garden'),
    path('digit/<int:pk>/', DigitView.as_view(), name='digit'),
    path('digit/delete/<int:pk>/', DeleteDigitView.as_view(), name='delete-digit'),
]
