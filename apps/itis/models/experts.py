from django.db import models


class Experts(models.Model):
    '''
    A taxonomist who is the responsible source for an occurrence of Taxonomic Units being
    recognized by and added to the ITIS database, or for changes being made to an
    occurrence of Taxonomic Units existing in the ITIS database, or who provides credibility
    for vernacular names.

    expert_id_prefix: A prefix attached to a serial number to identify the record as existing in Experts.
    expert_id: The unique identifier established for a specific expert in the field of taxonomy whose work is being utilized by the ITIS.
    expert: The name of the taxonomic expert providing credence to the taxonomy, nomenclature or attributes of a Taxonomic Unit’s occurrence for the ITIS.
    exp_comment: Remarks noted by or associated with a taxonomic expert who is providing credence to the taxonomy, nomenclature or attributes of a Taxonomic Unit’s occurrence.
    update_date: The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    '''
    expert_id_prefix = models.CharField(max_length=3, primary_key=True)
    expert_id = models.IntegerField(primary_key=True)
    expert = models.CharField(max_length=100)
    exp_comment = models.CharField(max_length=500, blank=True, null=True)
    update_date = models.DateField()

    class Meta:
        db_table = 'expert'
