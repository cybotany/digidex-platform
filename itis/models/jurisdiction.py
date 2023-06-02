from django.db import models


class Jurisdiction(models.Model):
    '''
    Association of a referenced occurrence of Taxonomic Units with one or more US
    jurisdictional units. Also provides an identification of whether the taxon was native
    and/or introduced to the unit.

    tsn: Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    jurisdiction_value: Label signifying a US jurisdictional unit as defined by the TWG, and Canada.
    origin: Indication of whether an occurrence of Taxonomic Units is native and/or introduced to a US jurisdictional unit.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    '''
    tsn = models.IntegerField(primary_key=True)
    jurisdiction_value = models.CharField(max_length=30, primary_key=True)
    origin = models.CharField(max_length=19)
    update_date = models.DateField()

    class Meta:
        db_table = 'jurisdiction'
