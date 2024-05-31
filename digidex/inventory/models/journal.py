import uuid
from django.db import models
from django.contrib import messages

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
    digit = models.OneToOneField(
        'inventory.InventoryDigit',
        on_delete=models.PROTECT,
        related_name='journal'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def add_entry(self, digit):
        journal_entry = Entry.objects.select_related('journal').create(
            journal=self,
            digit=digit
        )
        message = f"New entry created for '{digit.name}'!"
        messages.info(message)
        return journal_entry

    def get_entry(self, entry_number):
        try:
            return self.entries.select_related('journal').get(entry_number=entry_number)
        except Entry.DoesNotExist:
            return None

    def remove_entry(self, entry_number):
        entry = self.get_entry(entry_number)
        if entry:
            entry.delete()
            message = f"Entry '{entry_number}' was removed."
            messages.info(message)
        return None


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

    def __str__(self):
        return f"Journal Entry Collection: {self.uuid}"

    class Meta:
        verbose_name = "Journal Entry Collection"

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('digit').prefetch_related('entries')


class Entry(models.Model):
    journal = models.ForeignKey(
        EntryCollection,
        on_delete=models.CASCADE,
        related_name="entries"
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

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('journal')

    def __str__(self):
        return f"Entry on {self.created_at} for journal {self.journal.uuid}"
