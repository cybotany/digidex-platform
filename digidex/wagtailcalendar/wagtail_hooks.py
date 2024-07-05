from django.urls import path
from wagtail import hooks

from .views import index


@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('calendar/', index, name='calendar'),
    ]
