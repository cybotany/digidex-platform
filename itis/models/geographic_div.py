from django.db import models


class GeographicDiv(models.Model):
    '''
    Geographic association for the referenced occurrence in Taxonomic Units

    tsn: Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    geographic_value: Label given to a geographic division as identified by the Taxonomic Work Group.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.

    '''
    tsn = models.IntegerField(primary_key=True)
    geographic_value = models.CharField(max_length=45, primary_key=True)
    update_date = models.DateField()

    class Meta:
        db_table = 'geographic_div'
