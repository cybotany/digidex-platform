"""
digit URL Configuration
"""
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('user/', include('apps.accounts.urls')),
    path('api/', include('apps.api.urls')),
    path('digits/', include('apps.inventory.urls')),
    path('nfc/', include('apps.nfc.urls')),
]