from django.db import models


class Strippedauthor(models.Model):
    '''
    A support table that provides the author(s) associated with the name of a taxon with
    parenthesis, commas and periods removed. Designed to be helpful when searching for an
    author whose name contains a different punctuation for different taxon names.
    
    taxon_author_id: A unique identifier for the author(s) of a taxonomic name.
    shortauthor: The author(s) associated with the name of a taxon with parenthesis, commas and periods removed. Designed to be helpful when searching for an author whose name contains a different punctuation for different taxon names.
    '''
    taxon_author_id = models.IntegerField(primary_key=True)
    shortauthor = models.CharField(max_length=100)

    class Meta:
        db_table = 'strippedauthor'
