from django.db import models

from modelcluster import fields as mc_fields
from wagtail import models as wt_models
from wagtail.admin import panels

class BlogPageGalleryImage(wt_models.Orderable):
    page = mc_fields.ParentalKey(
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
        panels.FieldPanel('image'),
        panels.FieldPanel('caption'),
    ]
