from django.db import models


class ReferenceLinks(models.Model):
    '''
    An intersection table that provides a link between occurrences of Taxonomic Units and
    occurrences of publications, experts, or other_sources.

    tsn: Taxonomic Serial Number. The unique identifier for an occurrence of Taxonomic Units.
    doc_id_prefix: A designation affixed to the documentation_id identifying the reference as a publication, expert or other source.
    documentation_id: The serial portion of the identifier created for either the Publications table, the Experts table or the Other_Sources table used with the documentation_id_prefix to provide the reference link with an instance from the Taxonomic_units table.
    original_desc_ind: Indicator used to identify that this occurrence represents the reference of the original description, when available.
    init_itis_desc_ind: Indicator used to identify the reference(s) that serve as the reason for an occurrence of Taxonomic Units being recognized where the original reference is unavailable.
    change_track_id: The unique identifier assigned to a change made to an occurrence of Taxonomic Units.
    vernacular_name: A common name associated with an occurrence of Taxonomic Units.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    '''
    tsn = models.IntegerField(primary_key=True)
    doc_id_prefix = models.CharField(max_length=3, primary_key=True)
    documentation_id = models.IntegerField(primary_key=True)
    original_desc_ind = models.CharField(max_length=1, blank=True, null=True)
    init_itis_desc_ind = models.CharField(max_length=1, blank=True, null=True)
    change_track_id = models.IntegerField(blank=True, null=True)
    vernacular_name = models.CharField(max_length=80, blank=True, null=True)
    update_date = models.DateField()

    class Meta:
        db_table = 'reference_links'
