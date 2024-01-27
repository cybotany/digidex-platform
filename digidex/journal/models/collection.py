import os
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from digidex.journal.models import Entry
from digidex.utils.validators import validate_digit_thumbnail

def thumbnail_directory_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f'digit-{instance.id}/thumbnail{ext}'


class Collection(models.Model):
    """
    Aggregates journal entries for a single Digit.

    Attributes:
        thumbnail (ImageField): A reference to the 'Digit' model.
        created_at (DateTimeField): The date/time the journal collection was created.
        last_modified (DateTimeField): The date/time the journal collection was modified.
    """
    thumbnail = models.ImageField(
        upload_to=thumbnail_directory_path,
        validators=[validate_digit_thumbnail],
        null=True,
        blank=True,
        help_text="Thumbnail image for the digitized plant."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the journal collection instance was created."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified",
        help_text="The date and time when the journal collection instance was last modified."
    )

    def create_journal_entry(self, content=None, image=None):
        """
        Creates a journal entry for this collection with the given content and image.
        If content is not provided, a default message is used.
        """
        if not content:
            content = "Default journal entry content"

        entry_image = None
        if image and isinstance(image, InMemoryUploadedFile):
            entry_image = image

        Entry.objects.create(
            collection=self,
            content=content,
            image=entry_image
        )

    class Meta:
        verbose_name = "Journal Collection"
        verbose_name_plural = "Journal Collections"
