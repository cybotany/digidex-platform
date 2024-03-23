from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import basics as _fields
from base.blocks import basics as _blocks
from base import models as _models


class HomePage(_models.BasePage):
    body = _fields.BaseStreamField(
        [
            ('hero', _blocks.BaseStructBlock()),
            ('solutions', _blocks.BaseStructBlock()),
            ('company', _blocks.BaseStructBlock()),
            ('features', _blocks.BaseStructBlock()),
            ('reviews', _blocks.BaseStructBlock()),
            ('support', _blocks.BaseStructBlock()),
            ('faq', _blocks.BaseStructBlock()),
            ('cta', _blocks.BaseStructBlock()),
        ]
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
