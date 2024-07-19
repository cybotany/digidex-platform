from django.urls import path, include

from category.views import CategoryDetailView

app_name = "category"
urlpatterns = [
    path("<slug:category_slug>/", CategoryDetailView.as_view(), name="category-detail"),
    path("<slug:category_slug>/<slug:item_slug>/", include('item.urls')),
]
