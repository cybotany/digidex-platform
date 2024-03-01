import os
from datetime import datetime
from django.db import models, transaction
from django.urls import reverse

from digidex.utils import custom_storage 

def journal_image_directory_path(instance, filename):
    """
    Generates a unique filename using a combination of the digit's ID
    and a unique identifier.
    """
    ext = os.path.splitext(filename)[1]
    # Use the current timestamp as a unique identifier
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    return f'journal-{instance.collection.id}/entry-{timestamp}{ext}'


class JournalEntry(models.Model):
    """
    Represents journal entries associated with a Digit.

    This model is used to record observations, notes, or any relevant information about a specific digitized plant. 
    It also supports attaching an image to each journal entry.

    Attributes:
        collection (ForeignKey): The Journal Collection this entry is a part of.
        entry_number (PositiveIntegerField): Numeric value indicating the entry number within the collection.
        content (TextField): The textual content of the journal entry.
        image (ImageField): An optional image associated with the journal entry, supporting specific file extensions.
        created_at (DateTimeField): The date and time when the journal entry was created, automatically set when the journal entry is created.
        last_modified (DateTimeField): The date and time when the journal entry was last modified, automatically set whenever the journal entry is edited.

    Methods:
        __str__: Returns a string representation of the journal entry.
    """
    collection = models.ForeignKey(
        'journal.Collection',
        on_delete=models.CASCADE,
        related_name='entries',
        help_text="The collection this journal entry belongs."
    )
    entry_number = models.PositiveIntegerField(
        verbose_name="Entry Number",
        help_text="Numeric value indicating the entry number within the collection.",
        default=0,
        editable=False
    )
    content = models.TextField(
        null=True,
        blank=True,
        verbose_name="Content",
        help_text="The textual content of the journal entry."
    )
    image = models.ImageField(
        upload_to=journal_image_directory_path,
        storage=custom_storage.PrivateMediaStorage(), 
        null=True,
        blank=True,
        help_text="(Optional) The image to save with the journal entry. Only .jpg, .png, and .jpeg extensions are allowed."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when this journal entry was created."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified",
        help_text="The date and time when this journal entry was last modified."
    )

    def __str__(self):
        return f"Journal Entry {self.entry_number} for Collection: {self.collection.id}"

    @transaction.atomic
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            collection = self.collection
            collection.thumbnail = self
            collection.save()

    @transaction.atomic
    def delete(self, *args, **kwargs):
        if self.collection.thumbnail == self:
            self.collection.thumbnail = None
            self.collection.save()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        """
        Returns the URL to the detail view of this journal entry.
        """
        return reverse('journal:entry', kwargs={'pk': self.id})

    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"
        ordering = ['-created_at']