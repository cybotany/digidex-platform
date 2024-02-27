from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Collection(models.Model):
    """
    Aggregates journal entries for a single Digit.

    Attributes:
        thumbnail (URLField): A URL to an image representing the thumbnail of the collection.
        content_type (ForeignKey): The type of the digit associated with this journal collection.
        object_id (PositiveIntegerField): The ID of the digit associated with this journal collection.
        context_object (GenericForeignKey): A reference to the digit associated with this journal collection.
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
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        limit_choices_to=models.Q(app_label='inventory', model='plant') | 
                          models.Q(app_label='inventory', model='pet'),
        help_text="The type of the digit associated with this journal collection."
    )
    object_id = models.PositiveIntegerField(
        null=True,
        help_text="The ID of the digit associated with this journal collection."
    )
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
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

    def save(self, *args, **kwargs):
        if self._state.adding and not self.content_type_id:
            self.content_type = ContentType.objects.get(app_label='inventory', model='plant')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('journal:collection', kwargs={'pk': self.id})

    def get_entity_name(self):
        """
        Returns the name of the associated Plant or Pet entity.
        """
        return self.content_object.name if self.content_object else "No Entity"

    def get_entity_description(self):
        """
        Returns the description of the associated Plant or Pet entity.
        """
        return self.content_object.description if self.content_object else "No Description"

    def get_entity_url(self):
        """
        Returns the URL to view the details of the associated Plant or Pet entity.
        """
        return self.content_object.get_absolute_url() if self.content_object else self.get_absolute_url()
    
    def get_entry_count(self):
        """
        Returns the number of entries in this collection.
        """
        return self.entries.count()

    def get_all_entries(self):
        return self.entries.all().order_by('-created_at')

    def get_summarized_content(self):
        """
        Concatenates and returns a summarized version of the content of all entries in the collection. 
        Each entry is prefixed with its creation date and time, formatted as 'Month Day, Year HH:MM AM/PM',
        and placed on a new line to act as a header for the content.
        """
        return '\n\n'.join(
            f"{entry.created_at.strftime('%B %d, %Y %I:%M %p')}:\n{entry.content}"
            for entry in self.entries.all()
        )

    def get_image_carousel_data(self):
        """Returns a list of image URLs for the entries in the collection."""
        return [entry.image.url for entry in self.entries.all() if entry.image]

    class Meta:
        verbose_name = "Journal Collection"
        verbose_name_plural = "Journal Collections"
