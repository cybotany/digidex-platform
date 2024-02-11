from collections import defaultdict
from django.db import models
from django.contrib.contenttypes.models import ContentType
from . import UnitComments, UnitReferences, Hierarchy

class Unit(models.Model):
    """
    Represents a taxonomic unit in the ITIS data model.

    Attributes:
        tsn (IntegerField): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
        unit_ind1 (CharField): Indicator of an occurrence of a plant hybrid at the generic level.
        unit_name1 (CharField): The singular or first part of a scientifically accepted label for an occurrence of Taxonomic Units.
        unit_ind2 (CharField): A hybrid indicator positioned between the first and second parts of a binomial or polynomial taxonomic name.
        unit_name2 (CharField): The second part of a scientifically accepted label for a binomial/polynomial occurrence of Taxonomic Units.
        unit_ind3 (CharField): A category indicator located within a polynomial taxonomic name.
        unit_name3 (CharField): The third portion of a scientifically accepted label for a polynomial occurrence of Taxonomic Units
        unit_ind4 (CharField): A category indicator located within a polynomial taxonomic name.
        unit_name4 (CharField): The fourth part of a scientifically accepted label for a polynomial occurrence of Taxonomic Units.
        unaccept_reason (CharField): The cause for an occurrence of Taxonomic Units being identified as not accepted/invalid under the usage element.
        credibility_rating (CharField): A subjective rating designation as determined by the Taxonomic Work Group reflecting the level of review and the perceived level of accuracy for an occurrence of Taxonomic Units and its associated attributes.
        completeness_rating (CharField):  A rating designation reflecting whether all known, named, modern species (extant or recently extinct) for that taxon were incorporated into ITIS at the time of review.
        currency_rating (CharField): A rating designation reflecting the year of revision/source for a group.
        created_at (DateTimeField): Date and time at which an occurrence of Taxonomic Units is initially loaded into the ITIS database.
        parent (ForeignKey): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units. The taxonomic serial number for the direct parent of the subject occurrence of Taxonomic Units.
        author (ForeignKey): A unique identifier for the author(s) of a taxonomic name.
        hybrid_author (ForeignKey): The unique identifier for the author(s) of a taxonomic name which has been identified as the second part of a hybrid formula. For example Agrostis L. X Polypogon Desf.
        kingdom (ForeignKey): A unique identifier for the highest level of the taxonomic hierarchy structure.
        rank (ForeignKey): A unique identifier for a specific level within the taxonomic hierarchy
        last_modified (DateTimeField): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
        uncertain_prnt_ind (CharField): Indicator for occurrences of Taxonomic Units where placement is uncertain.
        name_usage (CharField): Current standing of an occurrence of a Taxonomic Unit.
        complete_name (CharField): The unit indicators and unit name fields concatenated and trimmed to present entire scientific name, without taxon author. Designed to be helpful when searching for taxa by scientific name.
    """

    tsn = models.IntegerField(
        primary_key=True,
        db_column="tsn",
        verbose_name="Taxonomic Serial Number",
        help_text="The unique identifier for an occurrence of Taxonomic Units."
    )
    unit_ind1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Unit Indicator 1",
        help_text="Indicator of an occurrence of a plant hybrid at the generic level."
    )
    unit_name1 = models.CharField(
        max_length=35,
        null=True,
        blank=True,
        verbose_name="Unit Name 1",
        help_text="The singular or first part of a scientifically accepted label for an occurrence of Taxonomic Units."
    )
    unit_ind2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Unit Indicator 2",
        help_text="A hybrid indicator positioned between the first and second parts of a binomial or polynomial taxonomic name."
    )
    unit_name2 = models.CharField(
        max_length=35,
        null=True,
        blank=True,
        verbose_name="Unit Name 2",
        help_text="The second part of a scientifically accepted label for a binomial/polynomial occurrence of Taxonomic Units."
    )
    unit_ind3 = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Unit Indicator 3",
        help_text="A category indicator located within a polynomial taxonomic name."
    )
    unit_name3 = models.CharField(
        max_length=35,
        null=True,
        blank=True,
        verbose_name="Unit Name 3",
        help_text="The third portion of a scientifically accepted label for a polynomial occurrence of Taxonomic Units"
    )
    unit_ind4 = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Unit Indicator 4",
        help_text="A category indicator located within a polynomial taxonomic name."
    )
    unit_name4 = models.CharField(
        max_length=35,
        null=True,
        blank=True,
        verbose_name="Unit Name 4",
        help_text="The fourth part of a scientifically accepted label for a polynomial occurrence of Taxonomic Units."
    )
    unnamed_taxon_ind = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Unnamed Taxon Indicator",
        help_text="Indicator for an occurrence of Taxonomic Units that has not been assigned a name."
    )
    unaccept_reason = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Unaccepted Reason",
        help_text="The cause for an occurrence of Taxonomic Units being identified as not accepted/invalid under the usage element."
    )
    credibility_rating = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Credibility Rating",
        help_text="A subjective rating designation as determined by the Taxonomic Work Group reflecting the level of review and the perceived level of accuracy for an occurrence of Taxonomic Units and its associated attributes."
    )
    completeness_rating = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Completeness Rating",
        help_text="A rating designation reflecting whether all known, named, modern species (extant or recently extinct) for that taxon were incorporated into ITIS at the time of review."
    )
    currency_rating = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Currency Rating",
        help_text="A rating designation reflecting the year of revision/source for a group."
    )
    created_at = models.DateTimeField(
        verbose_name="Created At",
        help_text="Date and time at which an occurrence of Taxonomic Units is initially loaded into the ITIS database."
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True,
        blank=True,
        verbose_name="Parent TSN",
        help_text="The taxonomic serial number for the direct parent of the subject occurrence of Taxonomic Units."
    )
    author = models.ForeignKey(
        'taxonomy.Author',
        on_delete=models.SET_NULL,
        related_name='authored_units',
        null=True,
        blank=True,
        verbose_name="Author ID",
        help_text="A unique identifier for the author(s) of a taxonomic name."
    )
    hybrid_author = models.ForeignKey(
        'taxonomy.Author',
        on_delete=models.SET_NULL,
        related_name='authored_hybrid_units',
        null=True,
        blank=True,
        verbose_name="Hybrid Author ID",
        help_text="The unique identifier for the author(s) of a taxonomic name which has been identified as the second part of a hybrid formula."
    )
    kingdom = models.ForeignKey(
        'taxonomy.Kingdom',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Kingdom",
        help_text="A unique identifier for the highest level of the taxonomic hierarchy structure."
    )
    rank = models.ForeignKey(
        'taxonomy.Rank',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Rank",
        help_text="A unique identifier for a specific level within the taxonomic hierarchy."
    )
    last_modified = models.DateTimeField(
        verbose_name="Update Date",
        help_text="The date a record was last modified."
    )
    uncertain_parent_ind = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="Uncertain Parent Indicator",
        help_text="Indicator for occurrences of Taxonomic Units where placement is uncertain."
    )
    name_usage = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        verbose_name="Name Usage",
        help_text="Current standing of an occurrence of a Taxonomic Unit."
    )
    complete_name = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name="Complete Name",
        help_text="The unit indicators and unit name fields concatenated and trimmed to present entire scientific name, without taxon author. Designed to be helpful when searching for taxa by scientific name."
    )

    def __str__(self):
        """
        Returns a string representation of the taxonomic unit, using its complete name.

        Returns:
            str: A string representation of the taxonomic unit.
        """
        return self.complete_name

    def get_absolute_url(self):
        """
        Generates a URL to the ITIS (Integrated Taxonomic Information System) website using the TSN.

        Returns:
            str: The ITIS URL if TSN is available, otherwise an empty string.
        """
        return f"https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value={self.tsn}#null"

    def get_author_name(self):
        """
        Retrieves the name of the author associated with this taxonomic unit.
        
        Returns:
            str: The name of the author if available, otherwise a default string indicating no author.
        """
        if self.author:
            return self.author.name
        else:
            return "No author available"

    def get_vernacular_names(self):
        """
        Retrieves all vernacular names associated with this taxonomic unit, including the vernacular name,
        its language, vernacular id, and approval status.

        Returns:
            list of dicts: A list of dictionaries, each containing vernacular name, its id, language,
                           and approval status for the taxonomic unit.
        """
        vernaculars = self.vernacular_set.all().values('id', 'vernacular_name', 'vernacular_language', 'approved_ind')
        return list(vernaculars)

    def get_comments(self):
        """
        Retrieves all comments associated with this taxonomic unit, including the commentator name and the comment text.

        Returns:
            list of dicts: A list of dictionaries, each containing the comment ID, commentator name, and comment text
                           for each comment associated with the taxonomic unit.
        """
        comments = UnitComments.objects.filter(tsn=self) \
                                        .select_related('comment') \
                                        .values('comment__id', 'comment__commentator', 'comment__comment')
        return list(comments)

    def get_references(self):
        """
        Retrieves all references associated with this taxonomic unit, including the type of reference
        (publication, expert, etc.) and its details.

        Returns:
            list of dicts: A list of dictionaries, each containing details of the reference associated
                           with the taxonomic unit.
        """
        # Step 1: Group UnitReferences by ContentType
        unit_references = UnitReferences.objects.filter(tsn=self)
        content_type_ids = unit_references.values_list('content_type_id', flat=True).distinct()

        # Prepare a mapping of ContentType ID to a list of object_ids
        references_map = defaultdict(list)
        for ref in unit_references:
            references_map[ref.content_type_id].append(ref.object_id)

        # Step 2: Batch fetch references for each ContentType
        fetched_objects = {}
        for ct_id, object_ids in references_map.items():
            content_type = ContentType.objects.get_for_id(ct_id)
            model_class = content_type.model_class()
            objects = model_class.objects.in_bulk(object_ids)
            fetched_objects[ct_id] = objects

        # Step 3: Construct result using fetched objects
        result = []
        for ref in unit_references:
            ct_id = ref.content_type_id
            obj_id = ref.object_id
            fetched_obj = fetched_objects[ct_id].get(obj_id)
            if fetched_obj:
                detail = {
                    'type': ref.content_type.model,
                    'object_id': obj_id,
                    'original_description': ref.original_description_ind,
                    'details': str(fetched_obj),
                }
                result.append(detail)

        return result

    def get_geographic_values(self):
        """
        Retrieves all geographic values associated with this taxonomic unit.

        Returns:
            list of str: A list of geographic values for the taxonomic unit.
        """
        return list(self.geography_set.all().values_list('geography_value', flat=True))

    def get_jurisdiction_info(self):
        """
        Retrieves all jurisdiction information associated with this taxonomic unit, including
        jurisdiction values and origin information.

        Returns:
            list of dicts: A list of dictionaries, each containing jurisdiction value and origin
                        information for the taxonomic unit.
        """
        jurisdictions = self.jurisdiction_set.all().values('jurisdiction_value', 'origin')
        return list(jurisdictions)

    def get_hierarchy_info(self):
        """
        Retrieves hierarchy information associated with this taxonomic unit, including
        the hierarchy string, level, and children count.

        Returns:
            dict: A dictionary containing the hierarchy string, level, and children count
                  for the taxonomic unit, or None if no hierarchy information is found.
        """
        try:
            hierarchy = self.hierarchy_set.get()  # Assuming there's only one hierarchy per unit
            return {
                'hierarchy_string': hierarchy.hierarchy_string,
                'level': hierarchy.level,
                'children_count': hierarchy.children_count,
            }
        except Hierarchy.DoesNotExist:
            return None

    def get_synonyms(self):
        """
        Retrieves all synonyms for this taxonomic unit if it is the accepted name.
        
        Returns:
            QuerySet of Unit instances that are synonyms of this unit.
        """
        synonyms = Unit.objects.filter(synonyms__tsn=self.tsn)
        return synonyms

    class Meta:
        indexes = [
            models.Index(fields=['complete_name', 'name_usage']),
        ]
