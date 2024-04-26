from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.core.models import ClusterableModel


@register_snippet
class AuthenticatedNavbarButton(ClusterableModel):
    link = models.URLField(
        verbose_name="Link URL"
        )
    text = models.CharField(
        verbose_name="Button Text",
        max_length=255
    )
    fill = models.CharField(
        verbose_name="Button Fill",
        max_length=255, help_text="Outline or Solid"
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('link'),
                FieldPanel('text'),
                FieldPanel('fill'),
            ],
            heading="Authenticated User Button Configuration"
        ),
    ]

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Authenticated Navbar Button"
        verbose_name_plural = "Authenticated Navbar Buttons"

@register_snippet
class NonAuthenticatedNavbarButton(ClusterableModel):
    link = models.URLField(
        verbose_name="Link URL"
    )
    text = models.CharField(
        verbose_name="Button Text",
        max_length=255
    )
    fill = models.CharField(
        verbose_name="Button Fill",
        max_length=255,
        help_text="Outline or Solid"
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('link'),
                FieldPanel('text'),
                FieldPanel('fill'),
            ],
            heading="Non-Authenticated User Button Configuration"
        ),
    ]

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Non-Authenticated Navbar Button"
        verbose_name_plural = "Non-Authenticated Navbar Buttons"
