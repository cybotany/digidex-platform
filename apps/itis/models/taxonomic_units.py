from django.db import models
from django.urls import reverse


class TaxonomicUnits(models.Model):
    """
    Represents a taxonomic unit in the ITIS data model.

    Attributes:
        tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
        unit_ind1 (str): Indicator of an occurrence of a plant hybrid at the generic level.
        unit_name1 (str): The singular or first part of a scientifically accepted label
                          for an occurrence of Taxonomic Units.
        unit_ind2 (str): A hybrid indicator positioned between the first and second parts of a
                         binomial or polynomial taxonomic name.
        unit_name2 (str): The second part of a scientifically accepted label
                          for a binomial/polynomial occurrence of Taxonomic Units.
        unit_ind3 (str): A category indicator located within a polynomial taxonomic name.
        unit_name3 (str): The third portion of a scientifically accepted label for a
                          polynomial occurrence of Taxonomic Units
        unit_ind4 (str): A category indicator located within a polynomial taxonomic name.
        unit_name4 (str): The fourth part of a scientifically accepted label for a
                          polynomial occurrence of Taxonomic Units.
        n_usage (str): Current standing of an occurrence of a Taxonomic Unit. Note that the usage
                     column is deprecated and will be removed in the future. This attribute has
                     been replaced by name_usage.
        unaccept_reason (str): The cause for an occurrence of Taxonomic Units being identified as
                               not accepted/invalid under the usage element.
        credibility_rtng (str): A subjective rating designation as determined by the
                                Taxonomic Work Group reflecting the level of review and the perceived
                                level of accuracy for an occurrence of Taxonomic Units and its associated attributes.
        completeness_rtng (str):  A rating designation reflecting whether all known, named,
                                  modern species (extant or recently extinct) for that taxon
                                  were incorporated into ITIS at the time of review.
        currency_rating (str): A rating designation reflecting the year of revision/source for a group.
        phylo_sort_seq (int): A sequence for an occurrence of Taxonomic Units with ranks
                                   between kingdom and order, inclusive, that will allow output
                                   to be displayed in phylogenetic order.
        initial_time_stamp (datetime): Date and time at which an occurrence of Taxonomic Units is
                                       initially loaded into the ITIS database.
        parent_tsn (int): Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
                          The taxonomic serial number for the direct parent of the subject occurrence of Taxonomic Units.
        taxon_author_id (int): A unique identifier for the author(s) of a taxonomic name.
        hybrid_author_id (int): The unique identifier for the author(s) of a taxonomic name
                                which has been identified as the second part of a hybrid formula.
                                For example Agrostis L. X Polypogon Desf.
        kingdom_id (int): A unique identifier for the highest level of the taxonomic hierarchy structure.
        rank_id (int): A unique identifier for a specific level within the taxonomic hierarchy
        update_date (datetime): The date on which a record is modified. The purpose of this
                                element is to provide assistance to those downloading data on a periodic basis.
        uncertain_prnt_ind (str): Indicator for occurrences of Taxonomic Units where placement is uncertain.
        name_usage (str):  Current standing of an occurrence of a Taxonomic Unit.
                           A duplicate of usage element. Note usage values moved to
                           name_usage because “usage” is a SQL reserved word which sometimes causes issues
                           with database code.
        complete_name (str): The unit indicators and unit name fields concatenated and trimmed to
                             present entire scientific name, without taxon author. Designed to be helpful when
                             searching for taxa by scientific name.
    """

    tsn = models.IntegerField(
        primary_key=True,
        verbose_name="Taxonomic Serial Number"
    )
    unit_ind1 = models.CharField(
        max_length=1,
        null=True,
        blank=True
    )
    unit_name1 = models.CharField(
        max_length=35,
        null=True,
        blank=True
    )
    unit_ind2 = models.CharField(
        max_length=1,
        null=True,
        blank=True
    )
    unit_name2 = models.CharField(
        max_length=35,
        null=True,
        blank=True
    )
    unit_ind3 = models.CharField(
        max_length=7,
        null=True,
        blank=True
    )
    unit_name3 = models.CharField(
        max_length=35,
        null=True,
        blank=True
    )
    unit_ind4 = models.CharField(
        max_length=7,
        null=True,
        blank=True
    )
    unit_name4 = models.CharField(
        max_length=35,
        null=True,
        blank=True
    )
    unnamed_taxon_ind = models.CharField(
        max_length=7,
        null=True,
        blank=True
    )
    n_usage = models.CharField(
        max_length=12,
        null=True,
        blank=True
    )
    unaccept_reason = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    credibility_rtng = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    completeness_rtng = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    currency_rating = models.CharField(
        max_length=7,
        null=True,
        blank=True
    )
    phylo_sort_seq = models.SmallIntegerField(
        null=True,
        blank=True
    )
    initial_time_stamp = models.DateTimeField(
        auto_now_add=True
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        db_column='parent_tsn'
    )
    taxon_author_id = models.IntegerField(
        null=True,
        blank=True
    )
    hybrid_author_id = models.IntegerField(
        null=True,
        blank=True
    )
    kingdom = models.ForeignKey(
        'Kingdoms',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='taxonomic_units',
        db_column='kingdom_id'
    )
    rank = models.ForeignKey(
        'TaxonUnitTypes',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='taxonomic_units',
        db_column='rank_id'
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    uncertain_prnt_ind = models.CharField(
        max_length=3,
        null=True,
        blank=True
    )
    name_usage = models.CharField(
        max_length=12,
        null=True,
        blank=True
    )
    complete_name = models.CharField(
        max_length=300,
        null=True,
        blank=True
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
        Get the URL to view the details of this taxonomic unit.

        Returns:
            str: The URL to view the details of this taxonomic unit.
        """
        return reverse('taxonomy:describe_taxonomic_unit', args=[str(self.tsn)])
