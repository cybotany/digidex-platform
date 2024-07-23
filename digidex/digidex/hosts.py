from django.conf import settings
from django.contrib import admin

from django_hosts import patterns, host

from wagtail.admin import urls as cms_urls


host_patterns = patterns('',
    host(r'api', 'api.urls', name='api'),
    host(r'admin', admin.site.urls, name='admin'),
    host(r'cms', cms_urls, name='cms'),
    host(r'link', 'inventorytags.urls', name='link'),
    host(r'', settings.ROOT_URLCONF, name='default'),
)
