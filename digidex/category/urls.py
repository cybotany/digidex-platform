from django.urls import path, include

from category.views import CategoryDetailView

app_name = "category"
urlpatterns = [
    path("<slug:slug>/detail/", CategoryDetailView.as_view(), name="category-detail"),
    path("<slug:slug>/", include('item.urls')),
]
