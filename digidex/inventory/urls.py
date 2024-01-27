from django.urls import path
from .views import (DigitStorageView, DigitLinkView, DigitCreationView, DigitDetailsView, DigitModificationView, DigitDeletionView)

app_name = 'inventory'
urlpatterns = [
    path('digit-storage', DigitStorageView.as_view(), name='storage'),
    path('link/<str:serial_number>/', DigitLinkView.as_view(), name='linking'),
    path('create-digit/<str:serial_number>/', DigitCreationView.as_view(), name='creation'),
    path('view-digit/<uuid:uuid>/', DigitDetailsView.as_view(), name='details'),
    path('modify-digit/<uuid:uuid>/', DigitModificationView.as_view(), name='modification'),
    path('delete-digit/<uuid:uuid>/', DigitDeletionView.as_view(), name='deletion'),
]
