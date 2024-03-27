from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from base.blocks import SectionBlock

class HomePage(Page):
    """
    Landing page for project. Designed to efficiently communicate
    the value proposition of the product and/or service to the target audience.

    """
    body = StreamField([
        ('section', SectionBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Homepage"
