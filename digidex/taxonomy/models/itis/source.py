from django.db import models

class ItisSource(models.Model):
    """
    Represents references, other than persons or publications, that are taxonomically significant for
    additions or changes to occurrences of the Taxonomic_units table and/or associated data,
    or that provide credibility for vernacular names.

    Attributes:
        id (IntegerField): The unique identifier for a supplier of information, other than a person or publication.
        source_type (CharField): The type of supplier providing information to ITIS, e.g., database.
        source (CharField): The name of the supplier of information to the ITIS database.
        version (CharField): Number, date, or other identifier of the source indicating its version.
        acquisition_date (DateField): The date on which ITIS acquired the data from the source.
        source_comment (TextField): Remarks associated with the provider of information to ITIS.
        last_modified (DateTimeField): The date and time the record was last updated.
    """
    id = models.IntegerField(
        primary_key=True, 
        help_text="The unique identifier for a supplier of information, other than a person or publication."
    )
    source_type = models.CharField(
        max_length=10, 
        blank=True, 
        null=True, 
        help_text="The type of supplier providing information to ITIS, e.g., database."
    )
    source = models.CharField(
        max_length=64, 
        blank=True, 
        null=True, 
        help_text="The name of the supplier of information to the ITIS database."
    )
    version = models.CharField(
        max_length=10, 
        blank=True, 
        null=True, 
        help_text="Number, date, or other identifier of the source indicating its version."
    )
    acquisition_date = models.DateField(
        blank=True, 
        null=True, 
        help_text="The date on which ITIS acquired the data from the source."
    )
    source_comment = models.TextField(
        max_length=500, 
        blank=True, 
        null=True, 
        help_text="Remarks associated with the provider of information to ITIS."
    )
    last_modified = models.DateTimeField(
        blank=True, 
        null=True,  
        help_text="The date and time the record was last updated."
    )

    def __str__(self):
        return f"Misc. Source: {self.id} - {self.source}"

    class Meta:
        verbose_name = "Source"
        verbose_name_plural = "Sources"
