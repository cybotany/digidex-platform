from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
# Import your block classes here
from .blocks import CategoryPageBlock

class CategoryPage(Page):
    content = StreamField(
        CategoryPageBlock(),
        verbose_name="Page content",
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Category Page"
        verbose_name_plural = "Category Pages"


class ProductPage(Page):
    # If you want to include some fixed fields (like a main image, title, etc.) you can define them here
    # For simplicity, we're assuming all product details will be handled by the `ProductBlock`
    
    # StreamField to include detailed product information, features, and FAQs
    body = StreamField([
        ('product', ProductBlock()),
        ('faq_section', FAQSectionBlock(optional=True)),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Product Page"
        verbose_name_plural = "Product Pages"