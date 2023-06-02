from django.db import models


class NodcIds(models.Model):
    """
    A mechanism for maintaining the association between the NODC data applications and
    the ITIS database to support users’ needs.

    nodc_id: An identifier previously assigned to an occurrence of Taxonomic Units by the National Oceanographic Data Center.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    tsn: Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    """
    nodc_id = models.CharField(primary_key=True, max_length=12)
    update_date = models.DateField()
    tsn = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'nodc_ids'
