from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from .blocks import SectionBlock

class HomePage(Page):
    """
    Landing page for project. Designed to efficiently communicate
    the value proposition of the product and/or service to the target audience.

    """
    body = StreamField([
        ('section', SectionBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Homepage"
        template = "home/home_page.html"