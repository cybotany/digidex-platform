from django.urls import path

from inventory.views import CategoryDetailView, ItemDetailView

app_name = "inventory"
urlpatterns = [
    path("<slug:inventory_slug>/<slug:category_slug>/", CategoryDetailView.as_view(), name="category-detail"),
    path("<slug:inventory_slug>/<slug:category_slug>/<slug:item_slug>/", ItemDetailView.as_view(), name="item-detail"),
]
