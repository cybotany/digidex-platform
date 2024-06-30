from django.urls import path

from .views import InventoryPageAssetSectionView

app_name = 'inventory'
urlpatterns = [
    path('api/v2/inventory/<uuid:uuid>/asset-section/', InventoryPageAssetSectionView.as_view(), name='inventory-asset-section')
]
