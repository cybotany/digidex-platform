from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.images import get_image_model
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class SiteLogo(models.Model):
    logo = models.ForeignKey(
        get_image_model(),
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel("logo"),
    ]

    def __str__(self):
        return "Site Logo"

    class Meta:
        verbose_name = "Site Logo"
        verbose_name_plural = "Site Logos"
