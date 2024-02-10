from django.db import models


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
        name_usage (CharField): Current standing of an occurrence of a Taxonomic Unit. Note that the usage column is deprecated and will be removed in the future. This attribute has been replaced by name_usage.
        unaccept_reason (CharField): The cause for an occurrence of Taxonomic Units being identified as not accepted/invalid under the usage element.
        credibility_rtng (CharField): A subjective rating designation as determined by the Taxonomic Work Group reflecting the level of review and the perceived level of accuracy for an occurrence of Taxonomic Units and its associated attributes.
        completeness_rtng (CharField):  A rating designation reflecting whether all known, named, modern species (extant or recently extinct) for that taxon were incorporated into ITIS at the time of review.
        currency_rating (CharField): A rating designation reflecting the year of revision/source for a group.
        phylo_sort_seq (SmallIntegerField): A sequence for an occurrence of Taxonomic Units with ranks between kingdom and order, inclusive, that will allow output to be displayed in phylogenetic order.
        initial_time_stamp (DateTimeField): Date and time at which an occurrence of Taxonomic Units is initially loaded into the ITIS database.
        parent (ForeignKey): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units. The taxonomic serial number for the direct parent of the subject occurrence of Taxonomic Units.
        author (ForeignKey): A unique identifier for the author(s) of a taxonomic name.
        hybrid_author (ForeignKey): The unique identifier for the author(s) of a taxonomic name which has been identified as the second part of a hybrid formula. For example Agrostis L. X Polypogon Desf.
        kingdom (ForeignKey): A unique identifier for the highest level of the taxonomic hierarchy structure.
        rank (ForeignKey): A unique identifier for a specific level within the taxonomic hierarchy
        last_modified (DateTimeField): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
        uncertain_prnt_ind (CharField): Indicator for occurrences of Taxonomic Units where placement is uncertain.
        n_usage (CharField):  Current standing of an occurrence of a Taxonomic Unit. A duplicate of usage element. Note usage values moved to name_usage because “usage” is a SQL reserved word which sometimes causes issues with database code.
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
    n_usage = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        verbose_name="Name Usage",
        help_text="Current standing of an occurrence of a Taxonomic Unit."
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
    phylo_sort_sequence = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Phylogenetic Sort Sequence",
        help_text="A sequence for an occurrence of Taxonomic Units with ranks between kingdom and order, inclusive, that will allow output to be displayed in phylogenetic order."
    )
    initial_time_stamp = models.DateTimeField(
        verbose_name="Initial Time Stamp",
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
    geography = models.CharField(
        max_length=200,
        verbose_name="Geographic Value",
        help_text="The geographic value."
    )
    jurisdiction = models.CharField(
        max_length=30,
        help_text="Label signifying a US jurisdictional unit as defined by the TWG, and Canada."
    )

    class Meta:
        indexes = [
            models.Index(fields=['complete_name']),
        ]

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
