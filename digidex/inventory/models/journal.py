import uuid
from django.db import models

from base.utils.storage import PublicMediaStorage


def journal_image_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'journals/{instance.journal.uuid}/images/{uuid.uuid4()}.{extension}'


class JournalEntry(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Journal Entry Collection UUID"
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
        return super().get_queryset().select_related('page')

    def __str__(self):
        return f"Journal entry made on{self.created_at}."
