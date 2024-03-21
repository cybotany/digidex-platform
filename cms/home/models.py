from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from home import blocks as _hblocks

class HomePage(Page):
    hero_content = StreamField(
        [('hero_section', _hblocks.HeroSection())],
        null=True,
        blank=True,
        help_text="Content for the hero section of the homepage."
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_content"),
    ]
