from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail
from base.blocks.page import call_to_action, heading


class BasePage(Page):
    heading = wagtail.BaseStreamField(
        [
            ('heading', heading.HeadingBlock()),
        ],
        null=True,
        blank=False,
        use_json_field=True
    )
    
    call_to_action = wagtail.BaseStreamField(
        [
            ('cta', call_to_action.CallToActionBlock()),
        ],
        null=True,
        blank=False,
        use_json_field=True
    )

    class Meta:
        abstract = True

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('call_to_action'),
    ]


class BaseIndexPage(BasePage):
    pass

    class Meta:
        abstract = True
