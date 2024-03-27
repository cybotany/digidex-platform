from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from base import blocks as _blocks

class HomePage(Page):
    """
    Landing page for project. Designed to efficiently communicate
    the value proposition of the product and/or service to the target audience.
    """
    body = StreamField([
        ('digit_display', _blocks.DisplayDigitBlock()),
        ('button_display', _blocks.DisplayButtonBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Homepage"
