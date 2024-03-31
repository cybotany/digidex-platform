# base/models.py
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.blocks import StructBlock, TextBlock, ChoiceBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock

class FooterLinkBlock(StructBlock):
    title = models.CharField(max_length=255)
    url = models.URLField()
    category = ChoiceBlock(
        choices=(
            ('company', 'Company Information'),
            ('news', 'News & Events'),
            ('social', 'Social Links'),
        ),
        required=True
    )

class FooterContactBlock(StructBlock):
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    chat = models.URLField(max_length=255)

@register_setting
class FooterSettings(BaseGenericSetting):
    content = StreamField(
        [
            ('logo', ImageChooserBlock(icon="image")),
            ('paragraph', TextBlock(icon="pilcrow")),
            ('contact', FooterContactBlock()),
            ('link', FooterLinkBlock(icon="link")),
            ('copyright', CharBlock(required=False)),
            ('credits', CharBlock(required=False)),
        ],
        null=True,
        blank=True
    )

    panels = [
        FieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Footer Settings"