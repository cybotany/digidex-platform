from django.urls import path, include

from wagtail import urls as wagtail_urls

urlpatterns = [
    path('link/', include('inventorytags.urls')),
    path("", include(wagtail_urls)),
]
