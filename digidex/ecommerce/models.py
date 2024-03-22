from wagtail.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel

from base.blocks import basic_blocks as _bblocks
from base.fields import wagtail_fields as _wfields
from ecommerce import blocks as _blocks

class EcommerceIndexPage(Page):
    top_heading = _bblocks.BaseCharBlock(
        required=True
    )
    categories = _wfields.BaseStreamField(
        [
            ('category_link', _blocks.CategoryLinkBlock()),
        ],
        null=True,
        blank=True
    )
    products = _wfields.BaseStreamField(
        [
            ('product', _blocks.ProductBlock()),
        ],
        null=True,
        blank=True
    )
    faqs = _wfields.BaseStreamField(
        [
            ('faq', _blocks.FAQBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('categories'),
        StreamFieldPanel('products'),
        StreamFieldPanel('faqs'),
    ]
