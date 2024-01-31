from django.urls import path
from digidex.inventory.views import (DigitStorageView, DigitCreationView, DigitDetailView, DigitModificationView, DigitDeletionView)

app_name = 'inventory'
urlpatterns = [
    path('storage-system/', DigitStorageView.as_view(), name='digit-storage'),
    path('<str:serial_number>/creation', DigitCreationView.as_view(), name='digit-creation'),
    path('<str:serial_number>/details', DigitDetailView.as_view(), name='digit-details'),
    path('<str:serial_number>/modification/', DigitModificationView.as_view(), name='digit-modification'),
    path('<str:serial_number>/deletion/', DigitDeletionView.as_view(), name='digit-deletion'),
]
