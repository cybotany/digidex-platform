from django.db import models

class Expert(models.Model):
    """
    Represents a taxonomist who is the responsible source for an occurrence of a Taxonomic Unit being
    recognized by and added to the ITIS database, or for changes being made to an
    occurrence of Taxonomic Unit in the ITIS database, or who provides credibility
    for vernacular names.

    Attributes:
        expert_id (IntegerField): The unique identifier for the author(s) of a taxonomic name.
        expert (CharField): The name of the taxonomic expert providing credence to the taxonomy,
                            nomenclature or attributes of a Taxonomic Unit occurrence for the ITIS.
        expert_comment (str): Remarks noted by or associated with a taxonomic expert who is providing
                           credence to the taxonomy, nomenclature or attributes of a Taxonomic Unit occurrence.
        last_modified (datetime): The date and time the record was last modified.
    """
    expert_id = models.IntegerField(
        primary_key=True,
        editable=False,
        help_text="The unique identifier for the author(s) of a taxonomic name."
    )
    expert = models.CharField(
        max_length=100,
        null=True,
        help_text="The name of the taxonomic expert providing credence to the taxonomy, nomenclature or attributes of a Taxonomic Unit occurrence for the ITIS."
    )
    expert_comment = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        help_text="Remarks noted by or associated with a taxonomic expert who is providing credence to the taxonomy, nomenclature or attributes of a Taxonomic Unit occurrence."
    )
    last_modified = models.DateTimeField(
        null=True,
        blank=True,
        help_text="The date and time the record was last modified."
    )

    def __str__(self):
        return self.expert

    class Meta:
        verbose_name = "Taxon Expert"
        verbose_name_plural = "Taxon Experts"
