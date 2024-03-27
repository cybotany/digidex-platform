from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from base.blocks import PageHeading, PageContent

class HomePage(Page):
    """
    Landing page for project. Designed to efficiently communicate
    the value proposition of the product/service to the target audience.
    """
    body = StreamField(
        [
            ('heading', PageHeading()),
            ('content', PageContent()),
        ],
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
