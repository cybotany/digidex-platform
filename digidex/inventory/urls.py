from django.urls import path

from inventory.views import InventoryDetailView, InventoryListView


urlpatterns = [
    path("<slug:slug>/", InventoryDetailView.as_view(), name="inventory-detail"),
    path("", InventoryListView.as_view(), name="inventory-list"),
]
