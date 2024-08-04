from django.conf import settings
from django.urls import include, path

from search.views import search
from wagtail import urls as wagtail_urls

urlpatterns = [
    path("accounts/", include('allauth.urls')),
    path("search/", search, name="search"),
    path("link/", include('inventory.urls')),
    path("", include(wagtail_urls)),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
