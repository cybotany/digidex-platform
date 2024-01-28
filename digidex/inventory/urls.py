from django.urls import path
from .views import (DigitStorageView, LinkDigitView, DigitModificationView, DigitDeletionView)

app_name = 'inventory'
urlpatterns = [
    path('digit-storage', DigitStorageView.as_view(), name='storage'),
    path('link/<str:serial_number>/', LinkDigitView.as_view(), name='linking'),
    path('modify-digit/<uuid:uuid>/', DigitModificationView.as_view(), name='modification'),
    path('delete-digit/<uuid:uuid>/', DigitDeletionView.as_view(), name='deletion'),
]
