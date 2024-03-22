from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

class EcommerceIndexPage(Page):
    top_heading = blocks.CharBlock(required=True)
    categories = StreamField([
        ('category_link', CategoryLinkBlock()),
    ], null=True, blank=True)

    products = StreamField([
        ('product', ProductBlock()),
    ], null=True, blank=True)

    faqs = StreamField([
        ('faq', FAQBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('categories'),
        StreamFieldPanel('products'),
        StreamFieldPanel('faqs'),
    ]
