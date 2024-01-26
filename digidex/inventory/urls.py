from django.urls import path
from .views import (DigitCreationView, DigitStorageView, DigitDetailsView, DigitDeletionView, DigitModificationView)

app_name = 'inventory'
urlpatterns = [
    path('', DigitStorageView.as_view(), name='storage'),
    path('<uuid:uuid>/', DigitDetailsView.as_view(), name='details'),
    path('create/<uuid:uuid>/', DigitCreationView.as_view(), name='creation'),
    path('delete/<uuid:uuid>/', DigitDeletionView.as_view(), name='deletion'),
    path('modify/<uuid:uuid>/', DigitModificationView.as_view(), name='modification'),
]
