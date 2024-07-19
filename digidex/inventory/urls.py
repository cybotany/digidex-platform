from django.urls import path, include

app_name = "inventory"
urlpatterns = [
    path("<slug:slug>/", include('category.urls')),
]
