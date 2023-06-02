from django.db import models


class TaxonomicUnits(models.Model):
    '''
    Taxon name and associated attributes for levels of taxonomic hierarchy
    structure from kingdom to genus; below genus,
    binomials/polynomials are identified.

    tsn: Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    unit_ind1: Indicator of an occurrence of a plant hybrid at the generic level.
    unit_name1: The singular or first part of a scientifically accepted label for an occurrence of Taxonomic Units.
    unit_ind2: A hybrid indicator positioned between the first and second parts of a binomial or polynomial taxonomic name.
    unit_name2: The second part of a scientifically accepted label for a binomial/polynomial occurrence of Taxonomic Units.
    unit_ind3: A category indicator located within a polynomial taxonomic name.
    unit_name3: The third portion of a scientifically accepted label for a polynomial occurrence of Taxonomic Units.
    unit_ind4: A category indicator located within a polynomial taxonomic name.
    unit_name4:  The fourth part of a scientifically accepted label for a polynomial occurrence of Taxonomic Units.
    unnamed_taxon_ind: Indicator for occurrences of Taxonomic Units whose names represent unnamed taxa and are therefore not standard taxonomic names.
    name_usage: Current standing of an occurrence of a Taxonomic Unit. A duplicate of usage element. Note usage values moved to name_usage because “usage” is a SQL reserved word which sometimes causes issues with database code.
    unaccept_reason: The cause for an occurrence of Taxonomic Units being identified as not accepted/invalid under the usage element.
    credibility_rtng: A subjective rating designation as determined by the Taxonomic Work Group reflecting the level of review and the perceived level of accuracy for an occurrence of Taxonomic Units and its associated attributes.
    completeness_rtng: A rating designation reflecting whether all known, named, modern species (extant or recently extinct) for that taxon were incorporated into ITIS at the time of review.
    currency_rating: A rating designation reflecting the year of revision/source for a group.
    phylo_sort_seq: A sequence for an occurrence of Taxonomic Units with ranks between kingdom and order, inclusive, that will allow output to be displayed in phylogenetic order.
    initial_time_stamp: Date and time at which an occurrence of Taxonomic Units is initially loaded into the ITIS database.
    parent_tsn: The taxonomic serial number for the direct parent of the subject occurrence of Taxonomic Units.
    taxon_author_id: A unique identifier for the author(s) of a taxonomic name.
    hybrid_author_id: The unique identifier for the author(s) of a taxonomic name which has been identified as the second part of a hybrid formula. For example Agrostis L. X Polypogon Desf.
    kingdom_id: A unique identifier for the highest level of the taxonomic hierarchy structure.
    rank_id: A unique identifier for a specific level within the taxonomic hierarchy.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    uncertain_prnt_ind: Indicator for occurrences of Taxonomic Units where placement is uncertain.
    n_usage:
    complete_name: The unit indicators and unit name fields concatenated and trimmed to present entire scientific name, without taxon author. Designed to be helpful when searching for taxa by scientific name.
    '''
    tsn = models.IntegerField(primary_key=True)
    unit_ind1 = models.CharField(max_length=1, blank=True, null=True)
    unit_name1 = models.CharField(max_length=35)
    unit_ind2 = models.CharField(max_length=1, blank=True, null=True)
    unit_name2 = models.CharField(max_length=35, blank=True, null=True)
    unit_ind3 = models.CharField(max_length=7, blank=True, null=True)
    unit_name3 = models.CharField(max_length=35, blank=True, null=True)
    unit_ind4 = models.CharField(max_length=7, blank=True, null=True)
    unit_name4 = models.CharField(max_length=35, blank=True, null=True)
    unnamed_taxon_ind = models.CharField(max_length=1, blank=True, null=True)
    name_usage = models.CharField(max_length=12)
    unaccept_reason = models.CharField(max_length=50, blank=True, null=True)
    credibility_rtng = models.CharField(max_length=40)
    completeness_rtng = models.CharField(max_length=10, blank=True, null=True)
    currency_rating = models.CharField(max_length=7, blank=True, null=True)
    phylo_sort_seq = models.SmallIntegerField(blank=True, null=True)
    initial_time_stamp = models.DateTimeField()
    parent_tsn = models.IntegerField(blank=True, null=True)
    taxon_author_id = models.IntegerField(blank=True, null=True)
    hybrid_author_id = models.IntegerField(blank=True, null=True)
    kingdom_id = models.SmallIntegerField()
    rank_id = models.SmallIntegerField()
    update_date = models.DateField()
    uncertain_prnt_ind = models.CharField(max_length=3, blank=True, null=True)
    n_usage = models.TextField(blank=True, null=True)
    complete_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'taxonomic_units'
