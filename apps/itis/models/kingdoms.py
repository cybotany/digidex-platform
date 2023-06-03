from django.db import models


class Kingdoms(models.Model):
    '''
    The highest rank in the taxonomic hierarchy structure.

    kingdom_id: The unique identifier for the kingdom.
    kingdom_name: The name of the kingdom.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    '''
    kingdom_id = models.IntegerField(primary_key=True)
    kingdom_name = models.CharField(max_length=10)
    update_date = models.DateField()

    class Meta:
        db_table = 'kingdoms'
