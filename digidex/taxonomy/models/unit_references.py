from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from digidex.taxonomy.utils.constants import BINARY_CHOICE

class UnitReferences(models.Model):
    """
    Represents a link between occurrences of a Taxonomic Unit and occurrences of publications,
    experts, or other sources. This table facilitates the association of taxonomic units with their
    respective references, experts, or sources, indicating original descriptions and changes.

    Attributes:
        tsn (ForeignKey): The Taxonomic Serial Number (TSN) of the taxonomic unit. Links to a 'Unit' model.
        content_type (ForeignKey): A prefix identifying the reference type (Expert, Publication, Other Source).
        object_id (PositiveIntegerField): The identifier for a publication, expert, or other source, used in conjunction with reference_prefix.
        original_desc_ind (CharField): Indicator for the reference of the original description of the taxonomic unit.
        init_itis_desc_ind (CharField): Indicator for references serving as the basis for recognizing a taxonomic unit where the original reference is unavailable.
        change_track_id (IntegerField): The unique identifier assigned to a change made to a taxonomic unit.
        vernacular_name (CharField): A common name associated with a taxonomic unit.
        last_modified (DateTimeField): The date and time the record was last updated.
    """
    tsn = models.ForeignKey(
        'taxonomy.Unit',
        on_delete=models.CASCADE,
        db_column="tsn",
        help_text="Taxonomic Serial Number (TSN) for the Taxonomic Unit."
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField(
        null=True,
        help_text="Primary key of the referenced model."
    )
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )
    original_desc_ind = models.CharField(
        max_length=1, 
        blank=True, 
        null=True, 
        choices=BINARY_CHOICE,
        help_text="Indicator for the reference of the original description of the taxonomic unit."
    )
    init_itis_desc_ind = models.CharField(
        max_length=1, 
        blank=True, 
        null=True, 
        choices=BINARY_CHOICE,
        help_text="Indicator for references serving as the basis for recognizing a taxonomic unit where the original reference is unavailable."
    )
    change_track_id = models.IntegerField(
        blank=True, 
        null=True, 
        help_text="The unique identifier assigned to a change made to a taxonomic unit."
    )
    vernacular_name = models.CharField(
        max_length=80, 
        blank=True, 
        null=True, 
        help_text="A common name associated with a taxonomic unit."
    )
    last_modified = models.DateTimeField(
        help_text="The date and time the record was last updated."
    )

    def __str__(self):
        return f"{self.content_type}{self.object_id} - TSN: {self.tsn}"

    class Meta:
        unique_together = ('tsn', 'content_type', 'object_id')
        verbose_name = "Unit Reference"
        verbose_name_plural = "Unit References"
