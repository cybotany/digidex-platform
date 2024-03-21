from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from home import blocks as _hblocks

class HomePage(Page):
    hero_content = StreamField(
        [('hero_section', _hblocks.HeroSection())],
        null=True,
        blank=True,
        help_text="Content for the hero section of the homepage."
    )
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_content"),
            ],
            heading="Hero Section",
        ),
        FieldPanel('body'),
    ]
