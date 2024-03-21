from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField

class HomePage(Page):
    hero_content = StreamField(
        [('hero', HeroSectionBlock())],
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
