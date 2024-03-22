from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.blocks import basic_blocks as _bblocks
from base.fields import wagtail_fields as _wfields
from digidex.base import models as base_models
from ecommerce import blocks as _blocks

class EcommerceIndexPage(base_models.IndexPage):
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
        FieldPanel('categories'),
        FieldPanel('products'),
        FieldPanel('faqs'),
    ]
