from django.urls import path
from .views import (DigitStorageView, DigitLinkView, DigitModificationView, DigitDeletionView)

app_name = 'inventory'
urlpatterns = [
    path('digit-storage', DigitStorageView.as_view(), name='storage'),
    path('digit/<str:serial_number>/', DigitLinkView.as_view(), name='digit-link'),
    path('digit/<str:serial_number>/modification', DigitModificationView.as_view(), name='modification'),
    path('digit/<str:serial_number>/deletion', DigitDeletionView.as_view(), name='deletion'),
]
