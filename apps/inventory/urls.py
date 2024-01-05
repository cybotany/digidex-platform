from django.urls import path
from .views import (DigitCreationView, DigitStorageView, DigitDetailsView, DigitDeletionView)

app_name = 'inventory'
urlpatterns = [
    path('', DigitStorageView.as_view(), name='storage'),
    path('<int:pk>/', DigitDetailsView.as_view(), name='details'),
    path('create/<int:pk>/', DigitCreationView.as_view(), name='creation'),
    path('delete/<int:pk>/', DigitDeletionView.as_view(), name='deletion'),
]
