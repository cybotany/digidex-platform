from django.utils.translation import gettext_lazy as _

from base.models import AbstractIndexPage

class APIPage(AbstractIndexPage):
    class Meta:
        verbose_name = _('api page')
