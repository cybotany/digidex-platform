from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail_fields as _wfields,\
                        django_fields as _dfields
from digidex.base import models as base_models
from support import blocks as _sblocks

class SupportIndexPage(base_models.IndexPage):
    intro_heading = _dfields.BaseCharField(
        max_length=75
    )
    intro_text = _dfields.BaseTextField(
        max_length=150
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
