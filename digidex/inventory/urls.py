from django.urls import path
from .views import (DigitStorageView, DigitLinkView, DigitModificationView, DigitDeletionView)

app_name = 'inventory'
urlpatterns = [
    path('digit-storage', DigitStorageView.as_view(), name='storage'),
    path('digit/<uuid:uuid>/', DigitLinkView.as_view(), name='digit-link'),
    path('modify-digit/<uuid:uuid>/', DigitModificationView.as_view(), name='modification'),
    path('delete-digit/<uuid:uuid>/', DigitDeletionView.as_view(), name='deletion'),
]
