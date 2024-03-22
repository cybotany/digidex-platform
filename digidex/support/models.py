from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

class SupportIndexPage(Page):
    intro_heading = blocks.CharBlock(required=True)
    intro_text = blocks.TextBlock(required=True)
    contact_options = StreamField([
        ('contact_option', ContactOptionBlock()),
    ], null=True, blank=True)
    
    faqs = StreamField([
        ('faq', FAQBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('intro_heading'),
        StreamFieldPanel('intro_text'),
        StreamFieldPanel('contact_options'),
        StreamFieldPanel('faqs'),
    ]
