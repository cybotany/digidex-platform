from django.db import models


class VernRefLinks(models.Model):
    '''
    An intersection table that provides a link between occurrences of Vernaculars and
    occurrences of Publications, Experts, or Other_Sources.

    tsn: Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    doc_id_prefix: A designation affixed to the documentation_id identifying the reference as a publication, expert or other source.
    documentation_id: The serial portion of the identifier created for either the Publications table, the Experts table or the Other_Sources table used with the documentation_id_prefix to provide the reference link with an instance from the vernaculars table.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    vern_id: The serial portion of the identifier created for a vernacular name associated with an occurrence of a Taxonomic Unit.
    '''
    tsn = models.IntegerField(primary_key=True)
    doc_id_prefix = models.CharField(max_length=3, primary_key=True)
    documentation_id = models.IntegerField(primary_key=True)
    update_date = models.DateField()
    vern_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'vern_ref_links'
