from django.utils.translation import gettext_lazy as _

from base.models import AbstractDigiDexPage


class HomePage(AbstractDigiDexPage):
    class Meta:
        verbose_name = _('home page')
