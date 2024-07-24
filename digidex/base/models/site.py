from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import (
    Page,
    Collection,
)
from wagtail.fields import RichTextField
from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PublishingPanel,
)
from wagtail.snippets.models import register_snippet


@register_snippet
class SiteLogo(models.Model,
):
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


class AbstractSitePage(Page):
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )
    body = RichTextField(
        blank=True,
        null=True,
        verbose_name=_("body")
    )

    content_panels = Page.content_panels + [
        FieldPanel('collection'),
        FieldPanel('body'),
    ]

    def __str__(self):
        return self.title

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    class Meta:
        abstract = True
