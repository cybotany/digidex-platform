from django.utils.translation import gettext_lazy as _

from base.models import AbstractSitePage


class HomePage(AbstractSitePage):
    parent_page_types = [
        'wagtailcore.Page'
    ]

    class Meta:
        verbose_name = _('homepage')
