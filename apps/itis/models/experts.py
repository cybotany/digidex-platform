from django.db import models
from django.urls import reverse


class Experts(models.Model):
    """
    A taxonomist who is the responsible source for an occurrence of Taxonomic Units being
    recognized by and added to the ITIS database, or for changes being made to an
    occurrence of Taxonomic Units existing in the ITIS database, or who provides credibility
    for vernacular names.

    Attributes:
        expert_id_prefix (str): A prefix attached to a serial number to identify the record as existing in Experts.
        expert_id (int): The unique identifier established for a specific expert in the field of taxonomy whose work is being utilized by the ITIS.
        expert (str): The name of the taxonomic expert providing credence to the taxonomy, nomenclature or attributes of a Taxonomic Unit’s occurrence for the ITIS.
        exp_comment (str): Remarks noted by or associated with a taxonomic expert who is providing credence to the taxonomy, nomenclature or attributes of a Taxonomic Unit’s occurrence.
        update_date (datetime): The date on which a record is modified. The purpose of this element is to provide assistance to those downloading data on a periodic basis.
    """

    expert_id_prefix = models.CharField(
        max_length=3,
        default="EXP",
        editable=False,
        verbose_name="Expert ID Prefix"
    )
    expert_id = models.AutoField(
        primary_key=True,
        verbose_name="Expert ID"
    )
    expert = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Expert Name"
    )
    exp_comment = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Expert Comment"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Update Date"
    )

    def __str__(self):
        """
        Returns a string representation of the expert, using their name.

        Returns:
            str: A string representation of the expert.
        """
        return self.expert

    def get_absolute_url(self):
        """
        Get the URL to view the details of this expert.

        Returns:
            str: The URL to view the details of this expert.
        """
        return reverse('taxonomy:describe_expert', args=[str(self.expert_id)])
