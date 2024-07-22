from django.conf import settings
from django.urls import include, path

from wagtail import urls as wagtail_urls
from accounts import urls as account_urls

urlpatterns = [
    path("", include(account_urls)),
    path("", include(wagtail_urls)),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
