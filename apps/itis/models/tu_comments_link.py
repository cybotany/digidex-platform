from django.db import models


class TuCommentsLinks(models.Model):
    '''
    An intersection table which provides the means for establishing a many to many
    relationship between an occurrence of Taxonomic Units and associated Comments.

    tsn: Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    comment_id: The unique identifier for remarks associated with an occurrence of Taxonomic Units.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    '''
    tsn = models.IntegerField(primary_key=True)
    comment_id = models.IntegerField(primary_key=True)
    update_date = models.DateField()

    class Meta:
        db_table = 'tu_comments_links'
