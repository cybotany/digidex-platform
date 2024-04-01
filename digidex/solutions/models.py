from wagtail import fields
from wagtail.admin.panels import FieldPanel

from base import models as _models
from solutions import blocks as _sblocks


class SolutionsIndexPage(_models.BasePage):
    parent_page_types = ["home.HomePage"]

    solutions = fields.StreamField(
        _sblocks.SolutionsStreamBlock,
        null=True,
        blank=True,
        help_text="Solution sections"
    )

    features = fields.StreamField(
        _sblocks.FeaturesStreamBlock,
        null=True,
        blank=True,
        help_text="Feature sections"
    )

    content_panels = _models.BasePage.content_panels + [
        FieldPanel('solutions', heading="Solution Sections"),
        FieldPanel('features', heading="Feature Sections"),
    ]

    class Meta:
        verbose_name = "Solutions Index Page"
        verbose_name_plural = "Solutions Index Pages"


class SolutionsPage(_models.BasePage):
    pass
