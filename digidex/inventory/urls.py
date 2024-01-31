from django.urls import path
from digidex.inventory.views import (DigitStorageView, DigitCreationView, DigitDetailView, DigitModificationView, DigitDeletionView)

app_name = 'inventory'
urlpatterns = [
    path('storage-system/', DigitStorageView.as_view(), name='digit-storage'),
    path('<slug:slug>/creation', DigitCreationView.as_view(), name='digit-creation'),
    path('<slug:slug>/details', DigitDetailView.as_view(), name='digit-details'),
    path('<slug:slug>/modification/', DigitModificationView.as_view(), name='digit-modification'),
    path('<slug:slug>/deletion/', DigitDeletionView.as_view(), name='digit-deletion'),
]
