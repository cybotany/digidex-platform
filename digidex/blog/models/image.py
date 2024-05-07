from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
from wagtail.admin.panels import FieldPanel


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(
        'blog.BlogPage',
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(
        blank=True,
        max_length=250
    )

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
