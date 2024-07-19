from django.urls import path

from item.views import ItemDetailView


app_name = "item"
urlpatterns = [
    path("<slug:slug>/", ItemDetailView.as_view(), name="item-detail"),
]
