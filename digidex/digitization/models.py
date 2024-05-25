import uuid
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.fields import RichTextField


class DigitalObject(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        help_text="Digitized object name."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Digitized object description."
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=255,
        verbose_name="Digitized Object Slug"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    @property
    def digit_name(self):
        return self.name.title()

    @property
    def digit_description(self):
        if self.description:
            return self.description
        return "No description available."

    @property
    def digit_page(self):
        try:
            return DigitalObjectPage.objects.get(
                digital_object=self
            )
        except DigitalObjectPage.DoesNotExist:
            raise ObjectDoesNotExist("There's no page for this digitized object.")

    def __str__(self):
        return f"{self.digit_name}"


class DigitalObjectPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = RichTextField(
        blank=True
    )
    digital_object = models.ForeignKey(
        'digitization.DigitalObject',
        on_delete=models.PROTECT,
        related_name='page'
    )

    search_fields = Page.search_fields + [
        index.SearchField('heading', partial_match=True, boost=2)
    ]

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
    ]
