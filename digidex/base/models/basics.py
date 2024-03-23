from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail as _wagtail
from base.blocks.page import heading as _heading,\
                             cta as _cta


class BasePage(Page):
    heading = _wagtail.BaseStreamField(
        [
            ('heading', _heading.HeadingBlock()),
        ],
        null=True,
        blank=False,
        use_json_field=True
    )
    call_to_action = _wagtail.BaseStreamField(
        [
            ('cta', _cta.CallToActionBlock()),
        ],
        null=True,
        blank=False,
        use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('call_to_action'),
    ]

    class Meta:
        abstract = True


class BaseIndexPage(BasePage):
    pass

    class Meta:
        abstract = True
