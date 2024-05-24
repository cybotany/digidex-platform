import uuid
from django.apps import apps
from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Orderable


class JournalEntry(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+',
        help_text="Digitized object image."
    )
    caption = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        help_text="Image caption."
    )
    digit = models.OneToOneField(
        "digitization.DigitalObject",
        on_delete=models.CASCADE,
        related_name='journal_entries'
    )

    @property
    def digit_name(self):
        return self.digit.digit_name

    @property
    def digit_description(self):
        return self.digit.digit_description

    @property
    def image_caption(self):
        return self.caption

    @property
    def digit_inventory_page(self):
        return self.digit.page

    @property
    def digit_inventory_page_url(self):
        return self.digit_inventory_page.url

    @property
    def digit_detail_page(self):
        return self.digit.detail_page

    @property
    def digit_detail_page_url(self):
        return self.digit_detail_page.url
