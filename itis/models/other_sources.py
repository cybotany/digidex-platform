from django.db import models


class OtherSources(models.Model):
    '''
    References, other than persons or publications, that are taxonomically significant for
    additions or changes to occurrences of the Taxonomic_units table and/or associated data,
    or that provide credibility for vernacular names.

    source_id_prefix: A prefix attached to a serial id to identify the record as an Other Source.
    source_id: The unique identifier for a supplier of information, other than a person or publication, lending credence to the establishment of or changes to an occurrence of Taxonomic Units.
    source_type: The designation of the kind of supplier providing information to the ITIS (other than a person or publication); e.g. database.
    source: The name of the supplier of information, other than a person or publication, to the ITIS database. Examples include, among others, Catalogue of the Vascular Plants of Madagascar and Hawaiian Arthropod Checklist Database.
    version: Number, date or other identifying characteristic of the source which indicates the functionality and/or data at a point in time in the life of the system, database, etc.
    acquisition_date: The date on which ITIS acquired the data it is utilizing from a source other than a publication or expert.
    source_comment: Remarks associated with the provider of information to the ITIS (other than a person or publication).
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    '''
    source_id_prefix = models.CharField(max_length=3, primary_key=True)
    source_id = models.IntegerField(primary_key=True)
    source_type = models.CharField(max_length=10)
    source = models.CharField(max_length=64)
    version = models.CharField(max_length=10)
    acquisition_date = models.DateField()
    source_comment = models.CharField(max_length=500, blank=True, null=True)
    update_date = models.DateField()

    class Meta:
        db_table = 'other_sources'
