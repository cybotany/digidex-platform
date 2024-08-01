from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
    Orderable,
)


class FooterBanner(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):
    subtitle = models.CharField(
        max_length=50
    )
    title = models.CharField(
        max_length=100
    )
    cta_url = models.URLField(
        null=True,
        blank=True
    )
    cta_text = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.subtitle

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('translation_key', 'locale'), name='unique_translation_key_locale_base_footerbanner')
        ]
