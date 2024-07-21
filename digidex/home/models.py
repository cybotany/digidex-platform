from django.utils.translation import gettext_lazy as _

from base.models import AbstractIndexPage


class HomePage(AbstractIndexPage):
    class Meta:
        verbose_name = _('home page')


class AdminPage(AbstractIndexPage):
    class Meta:
        verbose_name = _('admin page')
