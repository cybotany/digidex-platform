from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PublishingPanel,
)

from wagtail.snippets.models import register_snippet
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.models import Orderable


ICON_CHOICES = [
    ('test', 'Test'),
]

class RelatedLink(Orderable):
    component = ParentalKey(
        "base.Component",
        on_delete=models.CASCADE,
        related_name='related_links'
    )
    text = models.CharField(
        max_length=50
    )
    url = models.URLField()

    panels = [
        FieldPanel('text'),
        FieldPanel('url'),
    ]


class RelatedIconLink(Orderable):
    component = ParentalKey(
        "base.Component",
        on_delete=models.CASCADE,
        related_name='related_icon_links'
    )
    icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES
    )
    text = models.CharField(
        max_length=50
    )
    url = models.URLField()


    panels = [
        FieldPanel('text'),
        FieldPanel('url'),
        FieldPanel('icon'),
    ]


@register_snippet
class DigiDexComponent(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    PublishingPanel,
    ClusterableModel
    ):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.TextField()
    copyright = models.TextField()

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('logo'),
                FieldPanel('description'),
                InlinePanel('related_icon_links', label="Support Links"),

            ],
            heading="Main Footer Information"
        ),
        MultiFieldPanel(
            [
                InlinePanel('related_links', label="Footer Links"),
            ], 
            heading="Footer Links"
        ),
        FieldPanel('copyright'),
    ]

    def __str__(self):
        return "Footer Configuration"
