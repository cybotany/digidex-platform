from django.utils.translation import gettext_lazy as _

from base.models import AbstractDigiDexPage


class HomePage(AbstractDigiDexPage):
    parent_page_types = [
        'wagtailcore.Page'
    ]
    subpage_types = [
        'inventory.UserInventoryIndex'
    ]
    class Meta:
        verbose_name = _('homepage')
