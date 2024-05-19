import uuid
from django.apps import apps
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index
from wagtail.fields import RichTextField

from digitization.models import DigitizedObject, DigitizedObjectJournalEntry



class DigitizedObjectJournalEntry(models.Model):
    digit = models.ForeignKey(
        DigitizedObject,
        on_delete=models.CASCADE,
        related_name='images'
    )
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

    class Meta:
        abstract = True



class JournalEntry(Orderable, DigitizedObjectJournalEntry):
    digit = models.OneToOneField(
        UserDigit,
        on_delete=models.CASCADE,
        related_name='journal_entries'
    )
    page = ParentalKey(
        UserDigitPage,
        on_delete=models.CASCADE,
        related_name='digit_journal_entries'
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
