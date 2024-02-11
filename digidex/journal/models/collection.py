from django.db import models
from django.urls import reverse


class Collection(models.Model):
    """
    Aggregates journal entries for a single Digit.

    Attributes:
        thumbnail (URLField): A URL to an image representing the thumbnail of the collection.
        created_at (DateTimeField): The date/time the journal collection was created.
        last_modified (DateTimeField): The date/time the journal collection was modified.
    """
    thumbnail = models.ForeignKey(
        'journal.Entry',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='journal_thumbnail',
        help_text="Reference to the entry that contains the thumbnail image."
    )
    digit = models.OneToOneField(
        'inventory.Digit',
        on_delete=models.CASCADE,
        related_name='journal_collection',
        help_text="The digit associated with this journal collection."
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

    def get_absolute_url(self):
        return reverse('journal:collection', kwargs={'pk': self.id})

    def get_digit_name(self):
        return self.digit.name if self.digit else "No Digit"

    def get_digit_description(self):
        return self.digit.description if self.digit else "No Description"

    def get_digit_url(self):
        return self.digit.get_absolute_url() if self.digit else self.get_absolute_url()

    def get_entry_count(self):
        """
        Returns the number of entries in this collection.
        """
        return self.entries.count()
