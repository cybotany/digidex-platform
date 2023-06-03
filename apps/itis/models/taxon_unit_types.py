from django.db import models


class TaxonUnitTypes(models.Model):
    '''
    Defines the levels associated with the taxonomic hierarchical structure and establishes the
    rank order for an occurrence of the Taxonomic Units.

    kingdom_id: A unique identifier for the highest level of the taxonomic hierarchy structure.
    rank_id: A unique identifier for a specific level within the taxonomic hierarchy.
    rank_name: The label associated with the specific level of a taxonomic hierarchy.
    dir_parent_rank_id: The unique identifier for the rank of the closest parent of an occurrence of Taxonomic Units as defined by the kingdom's rank rules.
    req_parent_rank_id: The unique identifier for the closest, required parent of an occurrence of Taxonomic Units as established by the respective kingdom's rank rules.
    update_date: The date  on which the record was last updated. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    '''
    kingdom_id = models.IntegerField(primary_key=True)
    rank_id = models.SmallIntegerField(primary_key=True)
    rank_name = models.CharField(max_length=15)
    dir_parent_rank_id = models.SmallIntegerField()
    req_parent_rank_id = models.SmallIntegerField()
    update_date = models.DateField()

    class Meta:
        db_table = 'taxon_unit_types'
