from django.urls import path
from .views import (DigitLinkView, DigitCreationView, DigitStorageView, DigitDetailsView, DigitDeletionView, DigitModificationView)

app_name = 'inventory'
urlpatterns = [
    path('', DigitStorageView.as_view(), name='storage'),
    path('link-digit/<uuid:link-uuid>/', DigitLinkView.as_view(), name='linking'),
    path('view-digit/<uuid:digit-uuid>/', DigitDetailsView.as_view(), name='details'),
    path('create-digit/<uuid:digit-uuid>/', DigitCreationView.as_view(), name='creation'),
    path('delete-digit/<uuid:digit-uuid>/', DigitDeletionView.as_view(), name='deletion'),
    path('modify-digit/<uuid:digit-uuid>/', DigitModificationView.as_view(), name='modification'),
]
