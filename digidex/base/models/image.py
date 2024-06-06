from django.db import models

from wagtail.images.models import Image, AbstractImage, AbstractRendition


class DigiDexImage(AbstractImage):
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        help_text="Image caption."
    )
    admin_form_fields = Image.admin_form_fields + (
        'caption',
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