import uuid
from django.db import models
from django.conf import settings
from django.contrib import messages
from django.urls import reverse

from base.utils.storage import PublicMediaStorage


def journal_image_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'journals/{instance.journal.uuid}/images/{uuid.uuid4()}.{extension}'

class EntryCollection(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Journal Entry Collection UUID"
    )
    digital_object = models.OneToOneField(
        'inventory.DigitalObject',
        on_delete=models.CASCADE,
        related_name='journal'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def list_entries(self):
        return self.entries.select_related('journal')

    def get_panel_details(self):
        return {
            'name': self._name,
            'description': self._description,
            'date': self._date,
            'image_url': self._image_url,
            'delete_url': self._delete_url,
            'update_url': self._update_url
        }

    def get_card_details(self):
        return {
            'name': self._name,
            'description': self._description,
            'last_modified': self._date,
            'pageurl': self._page_url # self.page.url if self.page else '#',
        }

    @property
    def display_name(self):
        return self.digital_object.display_name

    @property
    def display_description(self):
        return self.digital_object.display_description

    @property
    def display_date(self):
        return self.digital_object.display_date

    @property
    def image_url(self):
        return None

    @property
    def _page(self):
        if not hasattr(self, 'page'):
            from inventory.utils import get_or_create_inventory_journal_page
            get_or_create_inventory_journal_page(self)
        return self.page

    @property
    def page_url(self):
        return self.page.url

    @property
    def update_url(self):
        return reverse('inventory:update_journal', kwargs=self.slug_kwargs)

    @property
    def delete_url(self):
        return reverse('inventory:delete_journal', kwargs=self.slug_kwargs)

    def __str__(self):
        return f"Journal Entry Collection: {self.uuid}"

    class Meta:
        verbose_name = "Journal Entry Collection"

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('digital_object').prefetch_related('entries')


class Entry(models.Model):
    journal = models.ForeignKey(
        EntryCollection,
        on_delete=models.CASCADE,
        related_name="entries"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="journal_entries",
    )
    image = models.ImageField(
        storage=PublicMediaStorage(),
        upload_to=journal_image_path,
        null=True,
        blank=True
    )
    entry_number = models.PositiveIntegerField(
        default=1,
        help_text="Entry number in the journal."
    )
    caption = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        help_text="Image caption."
    )
    note = models.TextField(
        blank=True,
        null=True,
        help_text="Journal entry note."
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def get_panel_details(self):
        return {
            'name': self._name,
            'description': self._description,
            'date': self._date,
            'image_url': self._image_url,
            'delete_url': self._delete_url,
            'update_url': self._update_url
        }

    def get_card_details(self):
        return {
            'name': self._name,
            'description': self._description,
            'last_modified': self._date,
            'pageurl': self._page_url # self.page.url if self.page else '#',
        }

    @property
    def _page(self):
        if not hasattr(self, 'page'):
            from inventory.utils import get_or_create_inventory_category_page
            get_or_create_inventory_category_page(self)
        return self.page

    @property
    def page_url(self):
        return self.page.url

    @property
    def update_url(self):
        return reverse('inventory:update_journal', kwargs=self.slug_kwargs)

    @property
    def delete_url(self):
        return reverse('inventory:delete_category', kwargs=self.slug_kwargs)

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('journal')

    def __str__(self):
        return f"Entry on {self.created_at} for journal {self.journal.uuid}"
