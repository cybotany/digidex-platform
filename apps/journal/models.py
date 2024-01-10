from django.db import models
from django.contrib.auth import get_user_model
from apps.inventory.models import Digit
from apps.utils.helpers import get_user_directory_path
from apps.utils.custom_storage import JournalImageStorage
from apps.utils.validators import validate_image_size_and_dimensions


class Entry(models.Model):
    """
    Represents journal entries associated with digitized plants.

    This model is used to record observations, notes, or any relevant information about a specific digitized plant. 
    It also supports attaching an image to each journal entry.

    Attributes:
        digit (ForeignKey): A reference to the 'Digit' model, linking the journal entry to a specific digitized plant.
        user (ForeignKey): The user who created the journal entry, linked to the user model.
        created_at (DateTimeField): The date and time when the journal entry was created, automatically set when the journal entry is created.
        content (TextField): The textual content of the journal entry.
        image (ImageField): An optional image associated with the journal entry, supporting specific file extensions.
        watered (BooleanField): Indicates whether the digitized plant was watered in this journal entry.
        fertilized (BooleanField): Indicates whether the digitized plant was fertilized in this journal entry.
        cleaned (BooleanField): Indicates whether the digitized plant was cleaned in this journal entry.

    Methods:
        __str__: Returns a string representation of the journal entry.
    """
    digit = models.ForeignKey(
        Digit,
        on_delete=models.CASCADE,
        related_name='journal_entries',
        help_text="The digitized plant to which this journal entry is related."
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="The user who created this journal entry."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when this journal entry was created."
    )
    content = models.TextField(
        verbose_name="Content",
        help_text="The textual content of the journal entry."
    )
    image = models.ImageField(
        upload_to=JournalImageStorage(get_user_directory_path),
        validators=[validate_image_size_and_dimensions],
        null=True,
        blank=True,
        help_text="(Optional) The image to save with the journal entry. Only .jpg, .png, and .jpeg extensions are allowed."
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

    def __str__(self):
        """
        Returns a string representation of the Journal Entry instance.

        The string representation includes information about the digitized plant and the user who created the journal entry.

        Returns:
            str: String representation of the Journal Entry instance.
        """
        return f"Journal Entry for {self.digit} by {self.user}"

    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"
        ordering = ['-created_at']