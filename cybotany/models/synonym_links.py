from django.db import models


class SynonymLinks(models.Model):
    '''
    A mechanism to provide the link between an accepted taxonomic name and alternates or
    predecessors to it.

    tsn: Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    tsn_accepted: The taxonomic serial number assigned to the accepted occurrence of Taxonomic Units to which a synonym is associated.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    '''
    tsn = models.IntegerField(primary_key=True)
    tsn_accepted = models.IntegerField(primary_key=True)
    update_date = models.DateField()

    class Meta:
        db_table = 'synonym_links'
