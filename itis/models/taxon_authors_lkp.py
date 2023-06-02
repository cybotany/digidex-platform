from django.db import models


class TaxonAuthorsLkp(models.Model):
    '''
    Reference to authors of taxa for all kingdoms.

    taxon_author_id: A unique identifier for the author(s) of a taxonomic name.
    taxon_author: The author(s) associated with the name of a taxon.
    update_date: The date  on which the record was last updated. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    kingdom_id: The unique identifier for the highest level of the taxonomic hierarchy structure.
    short_author: : The author(s) associated with the name of a taxon with parenthesis, commas and periods removed. Designed to be helpful when searching for an author whose name contains a different punctuation for different taxon names.
    '''
    taxon_author_id = models.IntegerField(primary_key=True)
    taxon_author = models.CharField(max_length=100)
    update_date = models.DateField()
    kingdom_id = models.SmallIntegerField()
    short_author = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'taxon_authors_lkp'
