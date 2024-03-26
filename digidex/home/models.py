from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    """
    Landing page for project. Designed to efficiently communicate
    the value proposition of the product and/or service to the target audience.

    """
    body = StreamField(
        [],
        default=[],
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
