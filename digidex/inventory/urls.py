from django.urls import path
from digidex.inventory.views import (DigitStorageView, DigitDetailsView, PublicDigitView, DigitModificationView, DigitDeletionView)

app_name = 'inventory'
urlpatterns = [
    path('storage/', DigitStorageView.as_view(), name='digit-storage'),    
    path('<uuid:uuid>/', DigitDetailsView.as_view(), name='digit-details'),
    path('<uuid:uuid>/public/', PublicDigitView.as_view(), name='public-digit'),
    path('<uuid:uuid>/modification/', DigitModificationView.as_view(), name='digit-modification'),
    path('<uuid:uuid>/deletion/', DigitDeletionView.as_view(), name='digit-deletion'),
]
