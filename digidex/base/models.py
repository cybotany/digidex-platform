from django.db import models
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel

from base.fields import basics as _fields


class BasePage(Page):
    pass

    class Meta:
        abstract = True


class BaseIndexPage(BasePage):
    pass

    class Meta:
        abstract = True


@register_setting
class CallToActionBanner(BaseGenericSetting):
    subtitle = _fields.BaseCharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Subtitle text"
    )
    heading = _fields.BaseCharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Main heading text"
    )
    call_to_action_page = _fields.BaseForeignKey(
        Page, null=True, blank=True, on_delete=models.SET_NULL, related_name="+", help_text="Page to link the call to action to"
    )

    panels = [
        FieldPanel('subtitle'),
        FieldPanel('heading'),
        PageChooserPanel('call_to_action_page'),
    ]
