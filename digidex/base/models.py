from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail as _wagtail
from base.blocks.page import heading as _blocks


class BasePage(Page):
    body = _wagtail.BaseStreamField(
        [
            ('heading', _blocks.HeadingBlock()),
        ],
        null=True,
        blank=False,
        use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        abstract = True


class BaseIndexPage(BasePage):
    pass

    class Meta:
        abstract = True
