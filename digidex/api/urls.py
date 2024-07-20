from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import InventoryTagViewSet

inventory_router = DefaultRouter()
inventory_router.register('ntags', InventoryTagViewSet)

urlpatterns = [
    path('inventory/', include(inventory_router.urls)),
]
