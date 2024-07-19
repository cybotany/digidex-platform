from django.urls import path

from inventory.views import InventoryDashboardView
from category.views import CategoryDetailView
from item.views import ItemDetailView

app_name = "inventory"
urlpatterns = [
    path("<slug:inventory_slug>/", InventoryDashboardView.as_view(), name="inventory-dashboard"),
    path("<slug:inventory_slug>/<slug:category_slug>/", CategoryDetailView.as_view(), name="category-detail"),
    path("<slug:inventory_slug>/<slug:category_slug>/<slug:item_slug>/", ItemDetailView.as_view(), name="item-detail"),
]
