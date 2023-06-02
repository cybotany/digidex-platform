from django.db import models


class Longnames(models.Model):
    '''
    A support table that provides a full scientific name without taxon author for Taxonomic
    Units.

    tsn: Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    completename: The unit indicators and unit name fields concatenated and trimmed to present entire scientific name, without taxon author. Designed to be helpful when searching for taxa by scientific name.
    '''
    tsn = models.IntegerField(primary_key=True)
    completename = models.CharField(max_length=300)

    class Meta:
        db_table = 'longnames'
