from django.urls import path, include

from api.views import inventory_router

urlpatterns = [
    path('inventory/', include(inventory_router.urls)),
]
