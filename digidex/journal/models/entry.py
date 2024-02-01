import os
from datetime import datetime
from django.db import models, transaction
from django.urls import reverse
from digidex.utils.custom_storage import PrivateMediaStorage
#from digidex.utils.validators import validate_journal_entry

def journal_image_directory_path(instance, filename):
    """
    Generates a unique filename using a combination of the digit's ID
    and a unique identifier.
    """
    ext = os.path.splitext(filename)[1]
    # Use the current timestamp as a unique identifier
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    return f'journal-{instance.id}/entry-{timestamp}{ext}'


class Entry(models.Model):
    """
    Represents journal entries associated with a Digit.

    This model is used to record observations, notes, or any relevant information about a specific digitized plant. 
    It also supports attaching an image to each journal entry.

    Attributes:
        collection (ForeignKey): The Journal Collection this entry is a part of.
        content (TextField): The textual content of the journal entry.
        image (ImageField): An optional image associated with the journal entry, supporting specific file extensions.
        is_thumbnail (BooleanField): Indicates if the entry's image is currently used as the thumbnail for the Collection.
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
    content = models.TextField(
        verbose_name="Content",
        help_text="The textual content of the journal entry."
    )
    image = models.ImageField(
        upload_to=journal_image_directory_path,
        storage=PrivateMediaStorage(), 
#        validators=[validate_journal_entry],
        null=True,
        blank=True,
        help_text="(Optional) The image to save with the journal entry. Only .jpg, .png, and .jpeg extensions are allowed."
    )
    is_thumbnail = models.BooleanField(
        default=False,
        verbose_name="Is Thumbnail",
        help_text="Indicates if the entry's image is currently used as the thumbnail for the Collection."
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
        return f"Journal Entry for Collection: {self.collection.id}"

    @transaction.atomic
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and not self.is_thumbnail:
            self.collection.entries.filter(is_thumbnail=True).update(is_thumbnail=False)
            self.is_thumbnail = True
            
            collection = self.collection
            collection.thumbnail = self.image.url
            collection.save()

    @transaction.atomic
    def delete(self, *args, **kwargs):
        if self.is_thumbnail:
            collection = self.collection
            collection.thumbnail = None
            collection.save()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        """
        Returns the URL to the detail view of this journal entry.
        """
        return reverse('journal:entry-details', kwargs={'pk': self.id})

    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"
        ordering = ['-created_at']