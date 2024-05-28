import uuid
from django.db import models

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
        'inventory.ItemizedDigit',
        on_delete=models.PROTECT,
        related_name='journal'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def add_entry(self, digit):
        journal_entry, created = Entry.objects.select_related('digit').get_or_create(
            journal=self,
            digit=digit
        )
        return journal_entry

    def get_all_entries(self):
        return self.entries.all() if self.entries.exists() else None

    def __str__(self):
        return f"Journal Entry Collection: {self.uuid}"

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
