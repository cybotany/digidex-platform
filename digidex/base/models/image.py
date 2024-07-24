from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.images.models import Image, AbstractImage, AbstractRendition


class BaseImage(AbstractImage):
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


class BaseRendition(AbstractRendition):
    image = models.ForeignKey(
        BaseImage,
        on_delete=models.CASCADE,
        related_name='renditions'
    )

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )
