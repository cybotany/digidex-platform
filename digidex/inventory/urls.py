from django.urls import path
from .views import (DigitLinkView, DigitCreationView, DigitStorageView, DigitDetailsView, DigitDeletionView, DigitModificationView)

app_name = 'inventory'
urlpatterns = [
    path('digit-storage', DigitStorageView.as_view(), name='storage'),
    path('link-digit/<uuid:link_uuid>/', DigitLinkView.as_view(), name='linking'),
    path('view-digit/<uuid:digit_uuid>/', DigitDetailsView.as_view(), name='details'),
    path('create-digit/<uuid:digit_uuid>/', DigitCreationView.as_view(), name='creation'),
    path('delete-digit/<uuid:digit_uuid>/', DigitDeletionView.as_view(), name='deletion'),
    path('modify-digit/<uuid:digit_uuid>/', DigitModificationView.as_view(), name='modification'),
]
