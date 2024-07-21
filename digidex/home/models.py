from django.utils.translation import gettext_lazy as _

from base.models import AbstractIndexPage


class HomePage(AbstractIndexPage):
    parent_page_types = [
        'wagtailcore.Page'
    ]

    class Meta:
        verbose_name = 'digidex homepage'
