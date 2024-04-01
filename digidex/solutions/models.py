from wagtail.admin.panels import FieldPanel

from base import models as _models
from solutions import blocks as _blocks


class SolutionsIndexPage(_models.BasePage):
    solutions = _blocks.SolutionsStreamBlock(
        [
            ('solution', _blocks.SolutionBlock(icon="placeholder")),
        ],
        null=True,
        blank=True,
        help_text="Solution sections"
    )

    features = _blocks.FeaturesStreamBlock(
        [
            ('feature', _blocks.FeatureBlock(icon="doc-full")),
        ],
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
