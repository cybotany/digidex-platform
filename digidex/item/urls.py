from django.urls import path

from item.views import ItemDetailView, ItemListView


urlpatterns = [
    path("<slug:slug>/", ItemDetailView.as_view(), name="item-detail"),
    path("", ItemListView.as_view(), name="item-list"),
]
