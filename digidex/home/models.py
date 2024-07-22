from django.utils.translation import gettext_lazy as _

from base.models import AbstractDigiDexPage


class DigiDexHomePage(AbstractDigiDexPage):
    parent_page_types = [
        'wagtailcore.Page'
    ]
    subpage_types = [
        'inventory.UserInventoryIndex'
    ]
    class Meta:
        verbose_name = _('digidex homepage')
