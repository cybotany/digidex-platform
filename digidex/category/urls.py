from django.urls import path

from category.views import CategoryDetailView, CategoryListView


urlpatterns = [
    path("<slug:slug>/", CategoryDetailView.as_view(), name="category-detail"),
    path("", CategoryListView.as_view(), name="category-list"),
]
