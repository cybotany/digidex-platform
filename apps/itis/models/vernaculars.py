from django.db import models


class Vernaculars(models.Model):
    '''
    Common names associated with an occurrence in Taxonomic Units.

    tsn: Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    vernacular_name: A common name associated with an occurrence of Taxonomic Units.
    language: Native language from which the vernacular name originates; e.g. English, French, Spanish, Portuguese, etc.
    approved_ind: Designation identifying those vernacular names authorized for use by regulation, statute, etc.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    vern_id: The serial portion of the identifier created for a vernacular name associated with an occurrence of a Taxonomic Unit.
    '''
    tsn = models.IntegerField(primary_key=True)
    vernacular_name = models.CharField(max_length=80)
    language = models.CharField(max_length=15)
    approved_ind = models.CharField(max_length=1, blank=True, null=True)
    update_date = models.DateField()
    vern_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'vernaculars'
