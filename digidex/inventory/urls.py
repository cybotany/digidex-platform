from django.urls import path
from .views import (DigitStorageView, DigitLinkView, DigitModificationView, DigitDeletionView)

app_name = 'inventory'
urlpatterns = [
    path('digit-storage', DigitStorageView.as_view(), name='storage'),
    path('digit/<uuid:uuid>/', DigitLinkView.as_view(), name='digit-link'),
    path('digit/<uuid:uuid>/modification', DigitModificationView.as_view(), name='modification'),
    path('digit/<uuid:uuid>/deletion', DigitDeletionView.as_view(), name='deletion'),
]
