from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import basics as _fields
from base.blocks import basics as _blocks
from base import models as _models


class SolutionIndexPage(_models.BaseIndexPage):
    pass


class SolutionPage(_models.BasePage):
    body = _fields.BaseStreamField(
        [
            ('heading', _blocks.BaseStructBlock()),
            ('solutions', _blocks.BaseStructBlock()),
            ('problems', _blocks.BaseStructBlock()),
            ('features', _blocks.BaseStructBlock()),
            ('benefits', _blocks.BaseStructBlock()),
            ('cta', _blocks.BaseStructBlock()),
        ],
        default=[],
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
