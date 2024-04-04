from django.db import models

from wagtail.admin import panels
from wagtail.snippets import models as wt_snippets

@wt_snippets.register_snippet
class Author(models.Model):
    name = models.CharField(
        max_length=255
    )
    author_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        panels.FieldPanel('name'),
        panels.FieldPanel('author_image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'
