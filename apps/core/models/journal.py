from django.db import models
from django.contrib.auth import get_user_model
from apps.utils.helpers import get_user_directory_path
from apps.utils.custom_storage import JournalImageStorage
from apps.utils.validators import validate_image_size_and_dimensions


class Journal(models.Model):
    """
    Model to represent journal entries for digitized plants.

    Attributes:
        digit (ForeignKey): The digitized plant to which the journal entry belongs.
        created_by (ForeignKey): The user who created the journal entry.
        created_at (DateTimeField): The date and time when the journal entry was created.
        entry (TextField): The content of the journal entry.
    """
    digit = models.ForeignKey(
        'Digit',
        on_delete=models.CASCADE,
        related_name='journal_entries'
    )
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="Created By"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    entry = models.TextField(
        verbose_name="Content"
    )
    image = models.ImageField(
        upload_to=JournalImageStorage(get_user_directory_path),
        validators=[validate_image_size_and_dimensions],
        null=True,
        blank=True,
        help_text="(Optional) The image to save with a journal entry. Only .jpg, .png, and .jpeg extensions are allowed."
    )

    def __str__(self):
        return f"Journal Entry for {self.digit} by {self.created_by}"

    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"
        ordering = ['-created_at']
