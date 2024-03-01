from collections import defaultdict
from django.db import models
from django.contrib.contenttypes.models import ContentType

from digidex.taxonomy.utils import constants as taxonomy_constants
from digidex.taxonomy.models.vernacular import references as vernacular_references

class Vernacular(models.Model):
    """
    Stores common names associated with Taxonomic Units, facilitating the inclusion of
    vernacular names in multiple languages and tracking their approval status.

    Attributes:
        - tsn (ForeignKey): The Taxonomic Serial Number (TSN) of the taxonomic unit. Links to a 'Unit' model.
        - id (IntegerField): Unique identifier for the vernacular name entry.
        - vernacular_name (CharField): Common name associated with the taxonomic unit.
        - vernacular_language (CharField): Language of the vernacular name.
        - approved_ind (CharField): Indicator of whether the vernacular name is approved.
        - last_modified (DateTimeField): Date and time when the record was last updated.
    """
    tsn = models.ForeignKey(
        'taxonomy.Unit',
        on_delete=models.CASCADE,
        db_column="tsn",
        help_text="Taxonomic Serial Number (TSN) for the Taxonomic Unit."
    )
    id = models.IntegerField(
        primary_key=True,
        help_text="Unique identifier for a vernacular name entry."
    )
    vernacular_name = models.CharField(
        max_length=80, 
        help_text="Common name associated with the taxonomic unit."
    )
    vernacular_language = models.CharField(
        max_length=15, 
        help_text="Language of the vernacular name."
    )
    approved_ind = models.CharField(
        max_length=1, 
        blank=True, 
        null=True, 
        choices=taxonomy_constants.BINARY_CHOICE,
        help_text="Indicator of whether the vernacular name is approved."
    )
    last_modified = models.DateTimeField(
        help_text="Date and time when the record was last updated."
    )

    def __str__(self):
        return f"{self.vernacular_name} ({self.vernacular_language}) - TSN: {self.tsn}"

    def get_references(self):
        """
        Retrieves all references associated with this vernacular name, including the type of reference
        (publication, expert, etc.) and its details.

        Returns:
            list of dicts: A list of dictionaries, each containing details of the reference associated
                           with the vernacular name.
        """
        # Fetch all VernacularReferences instances related to this Vernacular
        _v_refs = vernacular_references.VernacularReferences.objects.filter(vernacular=self)
        
        # Prepare a mapping of ContentType ID to a list of object_ids
        references_map = defaultdict(list)
        for ref in _v_refs:
            references_map[ref.content_type_id].append(ref.object_id)

        # Batch fetch references for each ContentType
        fetched_objects = {}
        for ct_id, object_ids in references_map.items():
            content_type = ContentType.objects.get_for_id(ct_id)
            model_class = content_type.model_class()
            objects = model_class.objects.in_bulk(object_ids)
            fetched_objects[ct_id] = objects

        # Construct result using fetched objects
        result = []
        for ref in _v_refs:
            ct_id = ref.content_type_id
            obj_id = ref.object_id
            fetched_obj = fetched_objects[ct_id].get(obj_id)
            if fetched_obj:
                detail = {
                    'type': ref.content_type.model,
                    'object_id': obj_id,
                    'details': str(fetched_obj),  # Assumes __str__ method of the referenced model provides meaningful info
                }
                result.append(detail)

        return result

    class Meta:
        unique_together = ('tsn', 'id')
        verbose_name = "Vernacular Name"
        verbose_name_plural = "Vernacular Names"
