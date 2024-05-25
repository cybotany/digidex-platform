import uuid
from django.db import models
from django.conf import settings

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
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="journal",
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def add_entry(self, digit):
        journal_entry, created = Entry.objects.get_or_create(
            user_party=self,
            digit=digit
        )
        return journal_entry

    def get_all_entries(self):
        return self.entries.all() if self.entries.exists() else None



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
