import os
from django.db import models
#from digidex.utils.validators import validate_digit_thumbnail

def thumbnail_directory_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f'journal-{instance.id}/thumbnail{ext}'


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
#        validators=[validate_digit_thumbnail],
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

    def get_digit_name(self):
        return self.digit.name if self.digit else "No Digit"

    def get_digit_description(self):
        return self.digit.description if self.digit else "No Description"

    class Meta:
        verbose_name = "Journal Collection"
        verbose_name_plural = "Journal Collections"
