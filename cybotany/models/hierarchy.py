from django.db import models


class Hierarchy(models.Model):
    '''
    A support table that provides an accepted or valid Taxonomic Units full TSN hierarchy in
    a single string.

    hierarchy_string: The concatenated TSNs, delimited with a hyphen, which represents the hierarchy from Kingdom to TSN of concern.
    tsn: Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    parent_tsn: The direct parent TSN of hierarchy.TSN.
    level: The distance down the hierarchy from Kingdom to TSN of concern for the hierarchy entry. For example, TSN 51, Schizomycetes, a Bacteria Class, has a level of 2.
    childrencount: The number of total children a particular TSN has, from its direct children to the bottom of the hierarchy.
    '''
    hierarchy_string = models.CharField(max_length=300, primary_key=True)
    tsn = models.IntegerField(primary_key=True)
    parent_tsn = models.IntegerField(blank=True, null=True)
    level = models.IntegerField()
    childrencount = models.IntegerField()

    class Meta:
        db_table = 'hierarchy'
