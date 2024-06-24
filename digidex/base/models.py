from django.db import models

from wagtail.images.models import Image, AbstractImage, AbstractRendition


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