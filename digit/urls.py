"""
digit URL Configuration
"""
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('api/', include('apps.api.urls')),
    path('', include('apps.core.urls')),
    path('inventory/', include('apps.inventory.urls')),
]