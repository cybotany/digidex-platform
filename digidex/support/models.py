from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.blocks import basic_blocks as _bblocks
from base.fields import wagtail_fields as _wfields
from base import models as _models
from support import blocks as _sblocks

class SupportIndexPage(_models.IndexPage):
    intro_heading = _bblocks.BaseCharBlock(
        required=True
    )
    intro_text = _bblocks.BaseTextBlock(
        required=True
    )
    contact_options = _wfields.BaseStreamField(
        [
            ('contact_option', _sblocks.ContactOptionBlock()),
        ],
        null=True,
        blank=True
    )
    faqs = _wfields.BaseStreamField(
        [
            ('faq', _sblocks.FAQBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro_heading'),
        FieldPanel('intro_text'),
        FieldPanel('contact_options'),
        FieldPanel('faqs'),
    ]
