from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail
from base.blocks.page import cta, heading


class BasePage(Page):
    body = wagtail.BaseStreamField(
        [
            ('heading', heading.HeadingBlock()),
            ('cta', cta.CallToActionBlock()),
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
