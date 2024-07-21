from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page, Collection
from wagtail.fields import RichTextField
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)

class DigiDexImage(AbstractImage):
    caption = models.TextField(
        blank=True,
        null=True,
        max_length=150
    )
    alt_text = models.CharField(
        blank=True,
        null=True,
        max_length=75
    )

    admin_form_fields = Image.admin_form_fields + (
        'caption',
        'alt_text',
    )


class DigiDexRendition(AbstractRendition):
    image = models.ForeignKey(
        DigiDexImage,
        on_delete=models.CASCADE,
        related_name='renditions'
    )

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )


class AbstractIndexPage(Page):
    parent_page_types = [
        'wagtailcore.Page'
    ]

    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )
    body = RichTextField(
        blank=True,
        null=True,
        verbose_name=_("body")
    )

    content_panels = [
        FieldPanel('body'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
