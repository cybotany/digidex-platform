import os
from datetime import datetime
from django.db import models
from digidex.utils.custom_storage import PrivateMediaStorage
from digidex.utils.validators import validate_journal_entry

def journal_image_directory_path(instance, filename):
    """
    Generates a unique filename using a combination of the instance's ID
    and a unique identifier.

    Args:
        instance: The model instance.
        filename: The original filename of the image.

    Returns:
        A unique filename.
    """
    ext = os.path.splitext(filename)[1]
    # Use the current timestamp as a unique identifier
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    return f'digit-{instance.digit.id}/entry-{timestamp}{ext}'


class Journal(models.Model):
    """
    Represents journal entries associated with digitized plants.

    This model is used to record observations, notes, or any relevant information about a specific digitized plant. 
    It also supports attaching an image to each journal entry.

    Attributes:
        digit (ForeignKey): A reference to the 'Digit' model, linking the journal entry to a specific digitized plant.
        watered (BooleanField): Indicates whether the digitized plant was watered in this journal entry.
        fertilized (BooleanField): Indicates whether the digitized plant was fertilized in this journal entry.
        cleaned (BooleanField): Indicates whether the digitized plant was cleaned in this journal entry.
        created_at (DateTimeField): The date and time when the journal entry was created, automatically set when the journal entry is created.
        content (TextField): The textual content of the journal entry.
        image (ImageField): An optional image associated with the journal entry, supporting specific file extensions.

    Methods:
        __str__: Returns a string representation of the journal entry.
    """
    digit = models.ForeignKey(
        'Digit', 
        on_delete=models.CASCADE,
        related_name='journal',
        help_text="The digitized plant to which this journal entry is related."
    )
    watered = models.BooleanField(
        default=False,
        verbose_name="Watered",
        help_text="Indicates whether the digitized plant was watered in this journal entry."
    )
    fertilized = models.BooleanField(
        default=False,
        verbose_name="Fertilized",
        help_text="Indicates whether the digitized plant was fertilized in this journal entry."
    )
    cleaned = models.BooleanField(
        default=False,
        verbose_name="Cleaned",
        help_text="Indicates whether the digitized plant was cleaned in this journal entry."
    )
    content = models.TextField(
        verbose_name="Content",
        null=True,
        blank=True,
        help_text="The textual content of the journal entry."
    )
    image = models.ImageField(
        upload_to=journal_image_directory_path,
        storage=PrivateMediaStorage(), 
        validators=[validate_journal_entry],
        null=True,
        blank=True,
        help_text="(Optional) The image to save with the journal entry. Only .jpg, .png, and .jpeg extensions are allowed."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when this journal entry was created."
    )

    def __str__(self):
        """
        Returns a string representation of the Journal Entry instance.

        The string representation includes information about the digitized plant.

        Returns:
            str: String representation of the Journal Entry instance.
        """
        return f"Journal Entry for {self.digit}"

    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"
        ordering = ['-created_at']